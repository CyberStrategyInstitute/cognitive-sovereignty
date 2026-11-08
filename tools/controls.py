"""Build domain control views from the shared catalog; preserve the six-domain model."""
import re
from tools.csf import ROOT, read_json


def validate(controls,domains):
    ids=[c['id'] for c in controls]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate mitigation ID')
    known={r['id'] for rows in read_json(ROOT/'taxonomy/registry.json').values() if isinstance(rows,list) for r in rows if isinstance(r,dict) and 'id' in r}
    for c in controls:
        if c['domain_id'] not in {d['id'] for d in domains}:raise ValueError('Unknown domain')
        if set(c['taxonomy'])-known:raise ValueError('Unknown control taxonomy link: '+c['id'])
        for key in ['implementation','owner_role','expected_outcome','test','failure_response','research_notes','rationale','evidence_status']:
            if not c.get(key):raise ValueError('Control missing '+key)
        for note in c['research_notes']:
            if not (ROOT/note).is_file():raise ValueError('Missing research note')
    mapped=[]
    for d in domains:
        mapped+=d['baseline_controls']+d['extension_controls']
        for cid in d['baseline_controls']+d['extension_controls']:
            if next(c for c in controls if c['id']==cid)['domain_id']!=d['id']:raise ValueError('Wrong domain mapping')
    if sorted(mapped)!=sorted(ids):raise ValueError('Every control needs one readiness profile')


def replace_block(text,key,body):
    block=f'<!-- {key}:start -->\n{body.rstrip()}\n<!-- {key}:end -->'
    pattern=rf'<!-- {re.escape(key)}:start -->.*?<!-- {re.escape(key)}:end -->'
    return re.sub(pattern,lambda _:block,text,flags=re.S) if re.search(pattern,text,re.S) else text+'\n'+block+'\n'


def views():
    controls=read_json(ROOT/'resources/controls.json');domains=read_json(ROOT/'resources/domains.json')
    validate(controls,domains)
    lines=['# Mitigation catalog','','Use the stable M-ID to connect research, implementation, assessment, and remediation. All 44 inherited IDs are retained; 20 are refined and 12 are added. Guidance is documented, not evidence of field effectiveness. See [the six-domain change assessment](../research/010_domain_controls_and_readiness.md) and [readiness worksheet](readiness-worksheet.md).','','[Search and filter controls](../docs/practice.html#controls) | [JSON](controls.json) | [Domain mappings](domains.json)','']
    results={}
    for d in domains:
        selected=[c for c in controls if c['domain_id']==d['id']]
        lines+=['## '+d['id']+': '+d['name'],'']
        for c in selected:
            lines += [f'<a id="{c["id"].lower()}"></a>','', '### '+c['id']+': '+c['name'],'',f"Status: {c['kind']}. Owner role: {c['owner_role']}. {c['evidence_status']}.",'',c['implementation'],'','Expected outcome: '+c['expected_outcome'],'','Check: '+c['test'],'','If it fails: '+c['failure_response'],'','Why: '+c['rationale'],'','Threats: '+', '.join(c['taxonomy'])+'. Research: '+', '.join(f'[{p.rsplit("/",1)[-1]}](../{p})' for p in c['research_notes'])+'.','']
        path=ROOT/d['path'];text=path.read_text(encoding='utf-8')
        a=text.index('## 4.');b=text.index('## 5.',a)
        rows=['## 4. Protective Capabilities and Mitigation Catalog','','Stable IDs connect each capability to its research and test. Existing IDs are retained. See the [full catalog](../resources/mitigation-catalog.md) for expected outcomes, owner roles, checks, and failure responses.','','| M-ID | Capability | Counters | Implementation | Research |','|---|---|---|---|---|']
        for c in selected:
            refs=', '.join(f'[{p.rsplit("/",1)[-1].split("_")[0]}](../{p})' for p in c['research_notes'])
            rows.append(f"| {c['id']} | {c['name']} ({c['kind']}) | "+', '.join(c['taxonomy'])+' | '+c['implementation']+' | '+refs+' |')
        text=text[:a]+'\n'.join(rows)+'\n\n---\n\n'+text[b:]
        for c in selected:
            if c.get('readiness_label'):
                row='| '+c['readiness_label']+' | '+' | '.join(c['readiness_anchors'][k] for k in ['0','3','5'])+' |'
                text=re.sub(r'^\| '+re.escape(c['readiness_label'])+r' \|.*$',lambda _:row,text,flags=re.M)
        exposure=['### Research-informed exposure updates','','These map additional mechanisms to existing threat IDs. They expand what this domain examines; they do not establish increased incidence, reach, or severity.','','| Existing threat ID | Mechanism to examine | Research |','|---|---|---|']
        for e in d['exposure_updates']:
            exposure.append('| '+e['taxonomy_id']+' ('+e['mapping_change']+') | '+e['mechanism']+' | '+', '.join(f'[{p.rsplit("/",1)[-1].split("_")[0]}](../{p})' for p in e['research_notes'])+' |')
        key='domain-exposure'
        if f'<!-- {key}:start -->' not in text:
            where=text.index('## 3.');text=text[:where]+f'<!-- {key}:start -->\n<!-- {key}:end -->\n\n'+text[where:]
        text=replace_block(text,key,'\n'.join(exposure))
        extra=['### Additional readiness checks','','Keep the inherited capability score and denominator unchanged. Report these research-extension checks separately. Unknown is not zero. Use [the worksheet](../resources/readiness-worksheet.md) and [worked unit example](../examples/unit_readiness_assessment.md). Readiness is a task-specific assessment, not CTSS.','','| M-ID | Check | 0 | 3 | 5 |','|---|---|---|---|---|']
        for c in selected:
            if c['kind']=='added':extra.append('| '+c['id']+' | '+c['test']+' | '+c['anchors']['0']+' | '+c['anchors']['3']+' | '+c['anchors']['5']+' |')
        extra+=['','Record the protocol, case set, catalog revision, date, assessor, evidence, failed cases, and remediation owner. No observed unit results were supplied, so current readiness remains unknown in all six domains. A documented capability is not a passed test.']
        key='domain-readiness'
        if f'<!-- {key}:start -->' not in text:
            start=text.index('Domain Readiness Assessment');where=text.index('\n## ',start)
            text=text[:where]+f'\n<!-- {key}:start -->\n<!-- {key}:end -->\n'+text[where:]
        text=replace_block(text,key,'\n'.join(extra))
        results[path]=text
    results[ROOT/'resources/mitigation-catalog.md']='\n'.join(lines).rstrip()+'\n'
    return results


def build():
    for path,text in views().items():path.write_text(text,encoding='utf-8',newline='\n')


if __name__=='__main__':build()
