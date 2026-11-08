"""Apply explicit lens input changes while preserving the shared baseline."""
import copy
from tools.csf import ROOT, WEIGHTS, read_json, score


def apply_lens(event, lens, profiles):
    if lens.get('baseline_id') != event.get('lens_id'):
        raise ValueError('Lens must name the event baseline')
    profile=next((p for p in profiles if p['id']==lens.get('lens_id')),None)
    if not profile or profile['baseline_id']!=event['lens_id']:
        raise ValueError('Unknown or incompatible lens')
    if profile.get('method')!='CTSS-existing-v1':
        raise ValueError('Lens must preserve the declared common CTSS method')
    if not lens.get('illustrative') and (not profile.get('sources') or 'template' in profile.get('version','')):
        raise ValueError('A template needs owner and source review before production use')
    if any(k in obj for obj in [lens,profile] for k in ['weights','formula']):
        raise ValueError('Lens cannot silently change CTSS weights or formula')
    if not lens.get('scope') or not lens.get('sources'):
        raise ValueError('Declare lens scope and evidence')
    values=copy.deepcopy(event['inputs'])
    for key,value in lens.get('input_changes',{}).items():
        if key not in WEIGHTS or not lens.get('reasons',{}).get(key):
            raise ValueError('Each changed input needs a reason')
        values[key]=value
    result=score(values)
    if result is None: raise ValueError('Lens score needs explicit inputs')
    return {'event_id':event['id'],'baseline_id':event['lens_id'],'lens_id':profile['id'],'illustrative':lens.get('illustrative',False),'scope':lens['scope'],'baseline_inputs':copy.deepcopy(event['inputs']),'baseline_score':score(event['inputs']),'lens_inputs':values,'lens_score':result,'score_difference':result-score(event['inputs']),'reasons':lens.get('reasons',{}),'limits':lens.get('limits','')}


def main():
    events={e['id']:e for e in read_json(ROOT/'research/intake/events.json')}
    profiles=read_json(ROOT/'lenses/profiles.json')
    results=[]
    for lens in read_json(ROOT/'lenses/examples.json'):
        before=copy.deepcopy(events[lens['event_id']])
        results.append(apply_lens(events[lens['event_id']],lens,profiles))
        assert before==events[lens['event_id']]
    import json
    (ROOT/'lenses/example-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for result in results:print(f"{result['event_id']}: baseline {result['baseline_score']}, illustrative lens {result['lens_score']}, change {result['score_difference']:+}.")


if __name__=='__main__':main()
