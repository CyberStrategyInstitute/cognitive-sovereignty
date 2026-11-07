"""Score evidenced domain capability checks separately from event CTSS."""
import argparse,json
from tools.csf import ROOT, read_json


def assess(record,controls=None,domains=None):
    controls=controls or read_json(ROOT/'resources/controls.json')
    domains=domains or read_json(ROOT/'resources/domains.json')
    known={c['id'] for c in controls};ratings={}
    for field in ['id','kind','assessment_date','scope','protocol','case_set','assessor','catalog_revision']:
        if not record.get(field):raise ValueError('Readiness record missing '+field)
    from datetime import date
    date.fromisoformat(record['assessment_date'])
    if record['kind'] not in {'observed','synthetic'}:raise ValueError('Unknown result kind')
    for row in record['ratings']:
        cid=row['control_id'];value=row.get('rating')
        if cid not in known or cid in ratings:raise ValueError('Unknown or repeated capability')
        if value is not None and (type(value) is not int or not 0<=value<=5):raise ValueError('Use whole ratings 0-5 or null')
        if value is not None and (not row.get('evidence') or not row.get('note')):raise ValueError('A known rating needs evidence and a reason')
        if value==5 and row.get('adverse_case_passed') is not True:raise ValueError('Rating 5 needs an adverse-case pass')
        ratings[cid]=row
    result=[]
    for d in domains:
        profiles={}
        for profile,key in [('legacy-v1','baseline_controls'),('research-extension-v1','extension_controls')]:
            ids=d[key];values=[ratings.get(cid,{}).get('rating') for cid in ids];count=sum(v is not None for v in values)
            profiles[profile]={'score':round(sum(values)/len(values)*20,1) if count==len(values) else None,'rated':count,'declared':len(values),'unknown':len(values)-count,'rating_sum':sum(v for v in values if v is not None),'scale':'0-5 capability ratings; higher means stronger demonstrated capability'}
        result.append({'domain_id':d['id'],'name':d['name'],'profiles':profiles})
    return {'assessment_id':record['id'],**{k:record[k] for k in ['kind','assessment_date','scope','protocol','case_set','assessor','catalog_revision']},'domains':result,'interpretation':'Training rubric, not validated fitness, clinical, employment, deployment, or CTSS scoring. Compare only the same protocol, case set, profile, and catalog revision.'}


def observed_summary():
    records=read_json(ROOT/'monitoring/readiness-assessments.json')
    assessed=[assess(r) for r in records]
    results=[r for r in assessed if r['kind']=='observed']
    return {'observed_assessments':len(results),'synthetic_excluded':sum(r['kind']=='synthetic' for r in records),'results':results,'status':'No observed unit results supplied; readiness unknown in all six domains' if not results else 'Task-specific observed assessments; compare matching protocols only'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('path',nargs='?');a=p.parse_args()
    path=(ROOT/a.path).resolve() if a.path else None
    if path and not path.is_relative_to(ROOT.resolve()):p.error('Use a record inside the repository')
    print(json.dumps(assess(read_json(path)) if path else observed_summary(),ensure_ascii=False,indent=2))
