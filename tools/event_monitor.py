"""Validate item-level CTSS records and build weekly research reports."""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from datetime import date
from tools.csf import ROOT, WEIGHTS, read_json, score, tier


def validate(events):
    ids=set()
    known={e['id'] for items in read_json(ROOT/'taxonomy/registry.json').values() if isinstance(items,list) for e in items if isinstance(e,dict) and 'id' in e}
    for event in events:
        for field in ['id','week_end','title','occurrences','original_analysis','taxonomy','theme','role','analysis','action','inputs','input_reasons','assessment_date','score_status','research_trigger']:
            if not event.get(field): raise ValueError(f"Event missing {field}: {event.get('id')}")
        if event['id'] in ids: raise ValueError('Duplicate event ID')
        ids.add(event['id'])
        if set(event['taxonomy'])-known: raise ValueError('Unknown taxonomy ID')
        if score(event['inputs']) is None: raise ValueError('Provisional scores need explicit estimates')
        if any(not event['input_reasons'].get(k) for k in WEIGHTS): raise ValueError('Missing score rationale')
        if event['role'] not in {'threat','protective','counterevidence','mixed','context'}: raise ValueError('Unknown evidence role')
        if event['score_status'] not in {'provisional','reviewed'}: raise ValueError('Unknown score status')
        if event['assessment_date'] < event['week_end']: raise ValueError('Assessment cannot predate the intake week')
        if event.get('lens_id','us-founding-v1')!='us-founding-v1': raise ValueError('Keep baseline records separate from optional lens outputs')
        date.fromisoformat(event['week_end']); date.fromisoformat(event['assessment_date'])
        for row in event.get('assessment_history',[]):
            date.fromisoformat(row['date'])
            if score(row['inputs']) is None or row['date']>=event['assessment_date']:
                raise ValueError('Historical assessments must preserve valid earlier inputs')
    return []


def aggregate(events):
    weeks=defaultdict(list)
    for event in events: weeks[event['week_end']].append(event)
    rows=[]
    for week,items in sorted(weeks.items()):
        threats=[e for e in items if e['role']=='threat']
        rows.append({'week_end':week,'items':len(items),'unique_story_threads':len({e.get('story_id',e['id']) for e in items}),'provisional':sum(e['score_status']=='provisional' for e in items),'mean_associated_risk':round(mean(score(e['inputs']) for e in items),1),'threat_items':len(threats),'mean_threat_risk':round(mean(score(e['inputs']) for e in threats),1) if threats else None,'high_or_critical':sum(score(e['inputs'])>=70 for e in items),'roles':dict(Counter(e['role'] for e in items)),'themes':dict(Counter(e['theme'] for e in items))})
    return rows


def revise(event, revision):
    """Preserve the prior assessment before applying a reasoned revision."""
    import copy
    from datetime import date
    if not revision.get('reason') or not revision.get('new_evidence'):
        raise ValueError('A revision needs a reason and new evidence or a documented correction')
    new_date=revision.get('date','')
    date.fromisoformat(new_date)
    if new_date <= event['assessment_date']:
        raise ValueError('Use a later revision date; preserve the original dated edition')
    if score(revision.get('inputs',{})) is None or any(not revision.get('input_reasons',{}).get(k) for k in WEIGHTS):
        raise ValueError('A revision needs five inputs and their reasons')
    result=copy.deepcopy(event)
    result.setdefault('assessment_history',[]).append({'date':event['assessment_date'],'inputs':event['inputs'],'input_reasons':event['input_reasons'],'score_status':event['score_status']})
    result.update(assessment_date=new_date,inputs=revision['inputs'],input_reasons=revision['input_reasons'],score_status='provisional',latest_revision_reason=revision['reason'],latest_revision_evidence=revision['new_evidence'])
    return result


def revision_trend(events):
    observations=[]
    dates=sorted({r['date'] for e in events for r in e.get('assessment_history',[])}|{e['assessment_date'] for e in events})
    for cutoff in dates:
        values=[]
        for event in events:
            history=event.get('assessment_history',[])+[{'date':event['assessment_date'],'inputs':event['inputs']}]
            available=[row for row in history if row['date']<=cutoff]
            if available:values.append(score(max(available,key=lambda r:r['date'])['inputs']))
        observations.append({'assessment_date':cutoff,'assessed_items':len(values),'mean_ctss':round(mean(values),1) if values else None})
    return observations


def slow_signals(events):
    weeks=defaultdict(set)
    for event in events:weeks[event['week_end']].add(event['theme'])
    streaks={};flags=[];previous=None
    for week,themes in sorted(weeks.items()):
        current=date.fromisoformat(week)
        if previous and (current-previous).days>8:streaks={}
        streaks={theme:streaks.get(theme,0)+1 for theme in themes}
        for theme,n in streaks.items():
            if n==3:flags.append({'week_end':week,'theme':theme,'collections':n,'trigger':'Research recurring mechanism; no automatic CTSS increase'})
        previous=current
    return sorted(flags,key=lambda r:(r['week_end'],r['theme']))


def merge_items(existing, incoming):
    """Add analyzed intake items; never silently overwrite an existing assessment."""
    import copy
    if not isinstance(incoming,list): raise ValueError('New intake must be a list of item records')
    result=copy.deepcopy(existing)
    ids={e['id'] for e in result}
    for event in incoming:
        if event.get('id') in ids:raise ValueError('Existing event ID: use a revision or link a new appearance')
        item=copy.deepcopy(event)
        import hashlib
        texts=[p['text'] for a in item.get('original_analysis',[]) for p in a.get('paragraphs',[])]
        item['original_analysis_sha256']=hashlib.sha256('\n'.join(texts).encode()).hexdigest()
        item.setdefault('story_id',item.get('id'))
        item.setdefault('assessment_history',[])
        result.append(item);ids.add(item.get('id'))
    validate(result)
    return result


def event_section(e):
    total=score(e['inputs'])
    lines=[f"## {e['id']}: {e['title']}",'',f"CTSS **{total}/100**, {tier(total)}. {e['score_status'].title()}; {e['role']} evidence. Intake week ends {e['week_end']}; assessed {e['assessment_date']}. Baseline: U.S. founding-principles lens v1.",'',e['analysis'],'',f"Framework links: {', '.join(e['taxonomy'])}. Theme: {e['theme']}.",'',f"Action: {e['action']}",'','| Input | Estimate | Reason |','|---|---|---|']
    for key in WEIGHTS:lines.append(f"| {key} | {e['inputs'][key]} | {e['input_reasons'][key]} |")
    lines+=['',f"Research trigger: {e['research_trigger']}",'',f"Source review: {e['source_review']}",'',f"Original score statement: {e['original_score_statement'] or 'No numerical or directional CTSS statement recovered for this item.'}",'']
    if e['source_urls']:lines.append('Sources: '+', '.join(f'[source {i}]({url})' for i,url in enumerate(e['source_urls'],1))+'.')
    else:lines.append('Source URL unresolved. The imported brief and paragraph locator are the present evidence record.')
    lines+=['',f"Original analysis retained in events.json; source occurrences: {', '.join(o['source_id'] for o in e['occurrences'])}.",'']
    return '\n'.join(line.rstrip() for line in lines)


def build(events):
    validate(events)
    out=ROOT/'research/intake/reports';out.mkdir(parents=True,exist_ok=True)
    summary=aggregate(events)
    manifest=read_json(ROOT/'research/intake/manifest.json')
    signals=read_json(ROOT/'research/intake/signals.json')
    lines=['# CSF weekly research baseline: September-November 2026','','Every supplied ranked or explicit context item is retained as an event-level record. Each has its own CTSS inputs, reasoning, framework impact, action, and research trigger. These are CSI working assessments backfilled on November 7, not scores claimed to have been issued during those earlier weeks.','','## Coverage','',f"Imported {len(manifest['files'])} files. Captured {len(events)} distinct assessed items across {len(summary)} intake weeks, {sum(len(e['occurrences']) for e in events)} item appearances, {len({e.get('story_id',e['id']) for e in events})} source-linked story threads, and {len(signals)} watch/action signals. Repeated UNESCO policy coverage is linked to one story instead of counted as independent policy evidence. A shared daily news digest is not treated as proof that two different studies are the same event. All original files are preserved in the local archive; complete Word paragraphs and links are retained under raw/. Headlines, original analysis, and alternate Markdown analysis remain in events.json.",'','The earlier six broad U.S. scenarios remain a separate scenario exercise. Their mean 53.2 is not the historical event baseline and must not be mixed into these trends.','','## Weekly assessment table','','| Week ending | Distinct items | Provisional | Mean associated-risk CTSS | Threat items | Mean threat-only CTSS | High/critical |','|---|---|---|---|---|---|---|']
    for r in summary:lines.append(f"| [{r['week_end']}]({r['week_end']}.md) | {r['items']} | {r['provisional']} | {r['mean_associated_risk']} | {r['threat_items']} | {r['mean_threat_risk'] if r['mean_threat_risk'] is not None else 'Not applicable'} | {r['high_or_critical']} |")
    lines+=['','These are retrospective intake-cohort means, assessed on November 7. They are not scores claimed to have been published each historical week. A week with different subject matter can have a different mean without the same threat becoming worse. Protective and counterevidence items receive a CTSS for the risk they illuminate; their evidence role records whether they may reduce or challenge that risk. A high associated-risk score does not label a helpful intervention harmful. No scores are subtracted to manufacture net protection.','','## Assessment revision history','','| Actual assessment date | Items assessed by then | Mean CTSS |','|---|---|---|']
    for row in revision_trend(events):lines.append(f"| {row['assessment_date']} | {row['assessed_items']} | {row['mean_ctss']} |")
    lines+=['','The backfill creates one actual scoring edition. Later revisions will add dates here without overwriting the first edition. New intake changes the cohort and must be distinguished from revisions to the same items.','','## Slow signals','','| Theme | Items in supplied intake |','|---|---|']
    for theme,n in Counter(e['theme'] for e in events).most_common():lines.append(f'| {theme} | {n} |')
    lines+=['','### Recurrence triggers recovered in this baseline','']
    for flag in slow_signals(events):lines.append(f"- {flag['week_end']}: {flag['theme']} appeared in three consecutive available collections. Research the repeated mechanism; this does not prove rising incidence or increase CTSS automatically.")
    lines+=['','These are coverage counts, not incidence rates. Omitted low-salience stories in the original Top 12 selections cannot be recovered. Going forward, record every scoped candidate, including low scores, stable findings, helpful evidence, and inconclusive signals. Flag repeated low-level observations in the same story/theme after three consecutive available weeks for research; this is an operational trigger, not a new CTSS multiplier.','','## Gaps and original scores','']
    lines += ['- '+gap for gap in manifest['coverage_gaps']]
    lines+=['','The inherited CTSS 90 reference is preserved with its original item. It is a family-level legacy statement, not an event-level five-input assessment. Original directional statements are retained verbatim. New provisional scores do not overwrite them.','','## Validation and correction','','A source record is not automatically accepted as fact. Legal allegations, platform claims, simulations, human experiments, policy proposals, and documented outcomes retain distinct evidence descriptions in the original analysis. Each provisional assessment states a research trigger. Review can revise any input; keep the previous dated revision and explain why. A reproduced score can still be a wrong judgment.','','Use the [intake method](../README.md) for future collection and the [lens assessment](../../../lenses/founding-baseline-assessment.md) for the baseline choice.']
    (out/'baseline.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    for week in sorted({e['week_end'] for e in events}):
        items=sorted((e for e in events if e['week_end']==week),key=lambda e:e['id'])
        header=f'# CSF research report: week ending {week}\n\nBackfilled November 7, 2026. Source of record: CSI analysis. All scores are provisional pending input review; the original analysis is preserved. CTSS uses the existing formula. Scores describe associated human-agency risk, while evidence roles distinguish threats, protective developments, counterevidence, mixed findings, and context.\n\n[Baseline and trends](baseline.md)\n\n'
        (out/(week+'.md')).write_text(header+'\n'.join(event_section(e) for e in items),encoding='utf-8')
    with (ROOT/'research/intake/event-scores.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f);writer.writerow(['id','week_end','assessed_on','title','role','theme','L','Ia','R','D','RecD','CTSS','status','research_trigger'])
        for e in sorted(events,key=lambda e:(e['week_end'],e['id'])):writer.writerow([e['id'],e['week_end'],e['assessment_date'],e['title'],e['role'],e['theme'],*[e['inputs'][k] for k in WEIGHTS],score(e['inputs']),e['score_status'],e['research_trigger']])
    (ROOT/'research/intake/weekly-trends.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'research/intake/slow-signal-flags.json').write_text(json.dumps(slow_signals(events),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    import hashlib
    receipt={'method':'event-intake-v1','assessment_as_of':max(e['assessment_date'] for e in events),'assessment_dates':sorted({e['assessment_date'] for e in events}),'baseline_id':'us-founding-v1','baseline_status':'Draft founding-principles profile; owner review pending','item_count':len(events),'item_appearances':sum(len(e['occurrences']) for e in events),'story_threads':len({e.get('story_id',e['id']) for e in events}),'roles':dict(Counter(e['role'] for e in events)),'source_files':len(manifest['files']),'provisional_scores':sum(e['score_status']=='provisional' for e in events),'sha256_utf8_lf':{name:hashlib.sha256((ROOT/name).read_text(encoding='utf-8').encode('utf-8')).hexdigest() for name in ['research/intake/events.json','research/intake/manifest.json','tools/event_monitor.py','lenses/profiles.json']}}
    (ROOT/'research/intake/report-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Built {len(summary)} weekly reports and {len(events)} individual CTSS assessments.')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['check','build','revise','ingest']);p.add_argument('--id');p.add_argument('--input',type=Path);args=p.parse_args()
    events=read_json(ROOT/'research/intake/events.json')
    validate(events)
    if args.command=='ingest':
        if not args.input:p.error('ingest needs --input')
        events=merge_items(events,read_json(args.input))
        (ROOT/'research/intake/events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        build(events)
        return
    if args.command=='revise':
        if not args.id or not args.input:p.error('revise needs --id and --input')
        matches=[i for i,e in enumerate(events) if e['id']==args.id]
        if not matches:raise ValueError('Unknown event ID')
        i=matches[0];events[i]=revise(events[i],read_json(args.input));validate(events)
        (ROOT/'research/intake/events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        build(events)
        return
    if args.command=='build':build(events)
    else:print(f'PASS: {len(events)} event records have unique IDs, valid taxonomy, five explicit inputs, and reasons.')


if __name__=='__main__':main()
