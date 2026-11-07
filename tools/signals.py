"""Track every imported watch/action excerpt without claiming it is a completed control."""
import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import date
from tools.csf import ROOT, read_json

PATH=ROOT/'research/intake/signals/register.json'
STATUSES={'reference','documented','planned','needs_research','watching','deferred','closed'}


def evidence_file(path):
    target=(ROOT/path).resolve()
    if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
        raise ValueError('Evidence must be an existing file inside the repository')
    return target


def bootstrap():
    if PATH.exists():raise ValueError('Signal register already exists; preserve its history')
    raw=read_json(ROOT/'research/intake/signals.json')
    events=read_json(ROOT/'research/intake/events.json')
    headings={0,3,5,7,9,11}
    deferred={13,48,128,158,199}
    groups={0:[1,2],3:[4],5:[6],7:[8],9:[10],11:[12]}
    parent={i:p for p,children in groups.items() for i in children}
    ids={i:'SIG-'+hashlib.sha256((r['source_id']+':'+str(r['paragraph'])).encode()).hexdigest()[:12] for i,r in enumerate(raw)}
    records=[]
    for i,r in enumerate(raw):
        text=r['text'].lower()
        if i in headings:kind,status='group_label','reference'
        elif i in deferred:kind,status='research_question','deferred'
        elif r['section']=='Adopt now':kind,status='action','documented'
        elif r['section']=='Investigate':kind,status='research_question','needs_research'
        elif r['section']=='Monitor':kind,status='watch','watching'
        else:kind,status='indicator','watching'
        if any(w in text for w in ['source','evidence','lineage','derivation','chart','verification']):
            theme='evidence integrity';links=['resources/advanced-checks.md','research/007_evidence_lineage.md']
        elif any(w in text for w in ['companion','relational','emotional','crisis','reciprocity','teen','guardian','self-harm']):
            theme='relational influence';links=['resources/advanced-checks.md','research/009_relational_influence.md']
        elif any(w in text for w in ['swarm','synthetic','deepfake','persona','identity','testimony','contributor']):
            theme='synthetic influence';links=['resources/advanced-checks.md','research/002_swarm_threat_scaling.md']
        elif any(w in text for w in ['authorization','permission','scope','stop','destructive','interlock','agent retries','reject','recourse']):
            theme='authorization and scope';links=['resources/advanced-checks.md','research/008_operator_objectives_and_persuasion.md']
        elif any(w in text for w in ['skill','learning','unaided','retention','offloading','independent','cognitive','reason','capability']):
            theme='retained capability';links=['resources/advanced-checks.md','research/006_independent_judgment.md']
        else:
            theme='oversight and recourse';links=['resources/advanced-checks.md','resources/practical-safeguards.md']
        matches=[]
        for e in events:
            for o in e['occurrences']:
                if o['source_id']==r['source_id'] and o['paragraph_start'] is not None and o['paragraph_start']<r['paragraph']:
                    matches.append((o['paragraph_start'],e['week_end']))
        week=max(matches)[1] if matches else None
        related=[e['id'] for e in events if e['week_end']==week and e['theme']==theme]
        if kind=='group_label':disposition='Source heading retained to preserve grouping; linked details carry the work.'
        elif status=='documented':disposition='Guidance is documented in the linked checks. Implementation and effectiveness in a real workflow are not established.'
        elif status=='deferred':disposition='Preserve the unchanged CTSS method. Revisit a modifier or new scoring mechanism after calibration evidence is available.'
        elif status=='needs_research':disposition='Research question retained. A study or protocol is required; no investigation result is claimed.'
        else:disposition='Await a source-backed observation in the next scoped weekly collection. Do not treat no observation as a zero score.'
        records.append({'id':ids[i],'source_id':r['source_id'],'source_paragraph':r['paragraph'],'source_section':r['section'],'source_text':r['text'],'source_week':week,'kind':kind,'group_id':ids[parent.get(i,i)],'theme':theme,'routing_status':'Initial routing for maintainer review; not a scored finding','status':status,'owner_role':'Framework maintainer' if status=='documented' else 'Research lead','assigned_to':None,'priority':'review_first' if any(w in text for w in ['crisis','destructive','irreversible','consent','vulnerable']) else 'normal','review_on':'2026-11-13','review_trigger':'New relevant evidence, a failed check, or three consecutive scoped collections with this mechanism. Review date is a proposed triage date, not an external commitment.','disposition':disposition,'evidence_paths':links,'related_event_ids':related,'validation_status':'Not field validated','history':[{'date':'2026-11-07','status':status,'note':disposition,'evidence_paths':links}]})
    PATH.parent.mkdir(parents=True,exist_ok=True)
    PATH.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return records


def validate(records):
    raw=read_json(ROOT/'research/intake/signals.json')
    originals={(r['source_id'],r['paragraph']):r['text'] for r in raw}
    events={e['id'] for e in read_json(ROOT/'research/intake/events.json')}
    ids=set()
    for r in records:
        if r['id'] in ids:raise ValueError('Duplicate signal ID')
        ids.add(r['id'])
        if originals.get((r['source_id'],r['source_paragraph']))!=r['source_text']:raise ValueError('Original signal text must remain intact')
        if r['status'] not in STATUSES or not r.get('owner_role') or not r.get('review_trigger') or not r.get('history'):raise ValueError('Signal needs status, role, trigger, and history')
        date.fromisoformat(r['review_on'])
        if r['status']=='closed' and (not r.get('closure_evidence') or not r.get('closure_note')):raise ValueError('Closure needs evidence and a reason')
        if set(r['related_event_ids'])-events:raise ValueError('Signal has an unknown event link')
        for path in r['evidence_paths']:
            evidence_file(path)
        for entry in r['history']:
            for path in entry.get('evidence_paths',[]):evidence_file(path)
        if r.get('closure_evidence'):evidence_file(r['closure_evidence'])
    if len(records)!=len(raw):raise ValueError('Every imported signal must have a tracker record')
    if any(r['group_id'] not in ids for r in records):raise ValueError('Unknown signal group')


def build(records):
    validate(records)
    counts=Counter(r['status'] for r in records)
    lines=['# Watch and action register','','Every imported excerpt has a stable ID, original source locator, disposition, responsible role, next review, and status history. Some excerpts are headings or indicators, so 217 excerpts do not mean 217 independent incidents or implementation projects. Named assignees remain unassigned; roles are proposed responsibilities.','','| Status | Count | Meaning |','|---|---|---|']
    meaning={'reference':'A grouping label, not an independent task','documented':'Written guidance exists; field implementation/validation remains open','planned':'An implementation task is retained','needs_research':'A study or investigation is needed','watching':'Await a relevant observation; review weekly','deferred':'Explicit decision to retain the question without changing the core scoring method','closed':'Closed only with an evidence record'}
    for status,n in sorted(counts.items()):lines.append(f'| {status} | {n} | {meaning[status]} |')
    lines+=['','## How to use it','','The searchable [research hub](../../../docs/research.html#signals) reads this same register. Use [CSV](register.csv) or [JSON](register.json) for tracking. Review items marked review_first, due items, new evidence, and repeated themes. An item cannot be closed without a reason and evidence. Documented does not mean deployed or effective.','','Run `python -m tools.signals check` to validate it. To update an item, use `python -m tools.signals update --id SIGNAL_ID --status STATUS --note "Reason" --evidence path/to/evidence.md --review-on YYYY-MM-DD`. This appends history and rebuilds the register views. Ownership changes must reflect actual assignment, not inferred participation.','','## Register','','| ID | Status | Role | Review | Original signal | Related work |','|---|---|---|---|---|']
    for r in records:
        escaped=r['source_text'].replace('|','\\|').replace('\n',' ')
        lines.append(f"| {r['id']} | {r['status']} | {r['owner_role']} | {r['review_on']} | {escaped} | "+', '.join(f'[{p.rsplit("/",1)[-1]}](../../../{p})' for p in r['evidence_paths'])+' |')
    (PATH.parent/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    with (PATH.parent/'register.csv').open('w',newline='',encoding='utf-8') as f:
        fields=['id','source_week','kind','theme','status','owner_role','assigned_to','priority','review_on','source_text','disposition']
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(records)
    print('Signal register:',dict(counts))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['bootstrap','build','check','update']);p.add_argument('--id');p.add_argument('--status',choices=sorted(STATUSES));p.add_argument('--note');p.add_argument('--evidence');p.add_argument('--review-on');a=p.parse_args()
    records=bootstrap() if a.command=='bootstrap' else read_json(PATH)
    validate(records)
    if a.command=='update':
        if not all([a.id,a.status,a.note,a.evidence,a.review_on]):p.error('Update needs ID, status, note, evidence, and review date')
        evidence_file(a.evidence)
        record=next((r for r in records if r['id']==a.id),None)
        if record is None:raise ValueError('Unknown signal ID')
        record.update(status=a.status,review_on=a.review_on,disposition=a.note)
        record['history'].append({'date':date.today().isoformat(),'status':a.status,'note':a.note,'evidence_paths':[a.evidence]})
        if a.status=='closed':record.update(closure_evidence=a.evidence,closure_note=a.note)
        validate(records);PATH.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if a.command!='check':build(records)
    else:print(f'PASS: {len(records)} source excerpts have valid tracking records.')


if __name__=='__main__':main()
