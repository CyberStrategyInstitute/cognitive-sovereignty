"""Read bounded CSF collections by stable ID. No network access or writes."""
import argparse
import json
from tools.csf import ROOT, read_json, score

COLLECTIONS={'events':'research/intake/events.json','signals':'research/intake/signals/register.json','lenses':'lenses/profiles.json','research':'research/evidence.json'}
COLLECTIONS.update(controls='resources/controls.json',domains='resources/domains.json',resources='resources/index.json',roadmap='monitoring/roadmap.json')
COLLECTIONS['pages']='docs/page-map.json'


def records(collection):
    if collection=='pages':return read_json(ROOT/COLLECTIONS[collection])['pages']
    if collection=='taxonomy':
        reg=read_json(ROOT/'taxonomy/registry.json')
        return [dict(entry,collection=key) for key,items in reg.items() if isinstance(items,list) for entry in items if isinstance(entry,dict) and 'id' in entry]
    if collection not in COLLECTIONS:raise ValueError('Unknown collection')
    return read_json(ROOT/COLLECTIONS[collection])


def query(collection, text='', limit=20, offset=0, week=None, status=None):
    if type(limit) is not int or not 1<=limit<=100 or type(offset) is not int or offset<0:raise ValueError('Use limit 1-100 and nonnegative offset')
    rows=records(collection)
    filtered=[r for r in rows if (not text or text.casefold() in json.dumps(r,ensure_ascii=False).casefold()) and (not week or r.get('week_end',r.get('source_week'))==week) and (not status or r.get('status',r.get('score_status'))==status)]
    # Return summaries by default; get_record provides the full provenance.
    fields=['id','title','name','source_text','week_end','source_week','assessment_date','status','score_status','theme','role','inputs','taxonomy','source_urls','analysis','disposition','review_on','domain_id','kind','implementation','expected_outcome','test','research_notes','path','outcome','priority','target','next_action','module','change','framework_version','source_owner','historical_body_preserved']
    results=[]
    for row in filtered[offset:offset+limit]:
        item={k:row[k] for k in fields if k in row}
        if 'inputs' in row:item['ctss']=score(row['inputs'])
        results.append(item)
    return {'schema_version':'1.0','collection':collection,'total':len(filtered),'offset':offset,'limit':limit,'next_offset':offset+limit if offset+limit<len(filtered) else None,'results':results}


def get_record(collection, record_id):
    for row in records(collection):
        if row['id']==record_id:return row
    raise ValueError('Unknown record ID')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('collection',choices=[*COLLECTIONS,'taxonomy']);p.add_argument('--id');p.add_argument('--text',default='');p.add_argument('--limit',type=int,default=20);p.add_argument('--offset',type=int,default=0);p.add_argument('--week');p.add_argument('--status');a=p.parse_args()
    try:result=get_record(a.collection,a.id) if a.id else query(a.collection,a.text,a.limit,a.offset,a.week,a.status)
    except (ValueError,KeyError) as exc:p.exit(1,str(exc)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
