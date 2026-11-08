"""Build repository headers, change labels, indexes, and navigation from owning records."""
import argparse
import hashlib
import html
import json
import os
import re
import xml.etree.ElementTree as ET
from collections import Counter,defaultdict
from pathlib import Path
from tools.csf import ROOT,read_json
from tools.version import VERSION

MODULES={
    '01-biological':('D1','Biological','F6921E'),
    '02-cognitive':('D2','Cognitive','127C9E'),
    '03-emotional':('D3','Emotional','9C4F83'),
    '04-social':('D4','Social','247563'),
    '05-purpose-moral':('D5','Purpose & Moral','7551A1'),
    '06-digital-ai-symbiosis':('D6','Digital & AI Symbiosis','820F1A'),
    'taxonomy':('TAX','Threat taxonomy','975100'),
    'research':('RES','Research and intelligence','145F80'),
    'resources':('USE','Controls and playbooks','246C59'),
    'examples':('EX','Examples and exercises','7551A1'),
    'monitoring':('MON','Monitoring and outcomes','8A3F53'),
    'lenses':('LENS','Baseline and perspectives','675185'),
    'integration':('API','Agent and MCP integration','126D87'),
    'schemas':('DATA','Data contracts','555E69'),
    'assets':('ART','Brand and visual assets','975100'),
    'tools':('TOOL','Build and assessment tools','246C59'),
    'tests':('QA','Verification checks','126D87'),
    'docs':('WEB','Web documentation','975100'),
    'command-center':('CMD','Legacy Command Center','820F1A'),
    '.github':('GOV','Contribution templates','555E69'),
}
INDEX_MODULES=['taxonomy','examples','tools','tests','docs','command-center']
STATUS_LABELS={'added':'NEW','refined':'UPDATED','inherited':'RETAINED'}


def files():
    result=[]
    for directory,dirs,names in os.walk(ROOT):
        dirs[:]=sorted(d for d in dirs if (not d.startswith('.') or d=='.github') and d not in {'node_modules','__pycache__'})
        for name in sorted(names):
            path=Path(directory)/name
            if path.suffix in {'.md','.html'}:result.append(path)
    return sorted(result,key=lambda path:path.relative_to(ROOT).as_posix())


def relative(source,target):
    return Path(os.path.relpath(ROOT/target,source.parent)).as_posix()


def managed(text,key,body,prepend=False):
    block=f'<!-- {key}:start -->\n{body.rstrip()}\n<!-- {key}:end -->'
    pattern=rf'<!-- {re.escape(key)}:start -->.*?<!-- {re.escape(key)}:end -->'
    if re.search(pattern,text,re.S):return re.sub(pattern,lambda _:block,text,flags=re.S)
    if prepend:return block+'\n\n'+text.lstrip()
    return text.rstrip()+'\n\n'+block+'\n'


def historical(path):
    name=path.relative_to(ROOT).as_posix()
    return name.startswith('monitoring/runs/') or bool(re.search(r'/reports/\d{4}-\d{2}-\d{2}\.md$',name)) or name=='research/proof-update-2026-11-07.md'


def change(path,baseline):
    name=path.relative_to(ROOT).as_posix()
    if name in baseline['comparison']['changes']:return baseline['comparison']['changes'][name]+' in 3.0'
    if name in baseline['standards_document_paths']:return 'NEW standards documentation'
    if name in baseline['pre_release_paths']:return 'RETAINED from pre-3.0 baseline'
    return 'NEW after published 3.0 baseline'


def title(path):
    text=path.read_text(encoding='utf-8')
    if path.suffix=='.html':
        match=re.search(r'<title>(.*?)</title>',text,re.S)
        return re.sub(r' \| CSF v[\d.]+$','',html.unescape(match[1])) if match else path.name
    match=re.search(r'^# (.+)',text,re.M)
    return re.sub(r'<[^>]+>','',match[1]).strip() if match else path.name


def role(path):
    name=path.relative_to(ROOT).as_posix()
    if historical(path):return 'Historical record; original body preserved'
    if name.startswith('examples/'):return 'Example or synthetic exercise; not observed readiness'
    if name.startswith('lenses/'):return 'Published documentation; lens profiles remain draft/templates'
    if name.startswith('research/intake/'):return 'Research intake; event CTSS judgments remain provisional'
    if name.startswith('research/'):return 'Research documentation; study and effectiveness limits apply'
    if name.startswith(('01-','02-','03-','04-','05-','06-','resources/')):return 'Documented guidance; field effectiveness not established'
    return 'Repository documentation; implementation limits remain explicit'


def decorate(path,text):
    """Keep generated-page producers and the final presentation pass idempotent."""
    if historical(path) or path.suffix!='.md':return text
    module=path.relative_to(ROOT).parts[0]
    if module in MODULES and path.name=='README.md':
        ident,label,color=MODULES[module]
        badge=relative(path,'assets/headers/'+module+'.svg')
        baseline=read_json(ROOT/'docs/repository-baseline.json')
        controls=read_json(ROOT/'resources/controls.json')
        counts=Counter(STATUS_LABELS[c['kind']] for c in controls if c['domain_id']==ident)
        text_status=f'CSF {VERSION}. Documentation: {change(path,baseline)}. {role(path)}.'
        if ident.startswith('D') and ident[1:].isdigit():text_status+=f" Control comparison: {counts['NEW']} NEW, {counts['UPDATED']} UPDATED, {counts['RETAINED']} RETAINED in 3.0. No controls are marked DEPRECATED."
        body=f'![{ident}: {label}. CSF {VERSION}. Status is repeated in text below.]({badge})\n\n{text_status}'
        badges=f'[![Framework {VERSION}]({relative(path,"assets/badges/version.svg")})]({relative(path,"VERSION")}) [![Documentation license: CC BY-SA 4.0]({relative(path,"assets/badges/docs-license.svg")})]({relative(path,"LICENSE")})'
        text=managed(text,'csf-module-header',body+'\n\n'+badges,prepend=True)
    elif path.parent==ROOT/'research' and re.match(r'\d{3}_',path.name):
        baseline=read_json(ROOT/'docs/repository-baseline.json')
        label=f'**{change(path,baseline)}.** Research note {path.name[:3]}. Published as documentation in CSF {VERSION}; proposal, source-review, and validation limits below remain in force.'
        text=managed(text,'csf-research-status',label,prepend=True)
    nav=f'[Repository home]({relative(path,"README.md")}) · [Complete page map]({relative(path,"PAGE_MAP.md")}) · [Resources]({relative(path,"resources/README.md")}) · [Research]({relative(path,"research/README.md")}) · [Data catalog]({relative(path,"docs/data/catalog.json")})'
    if module in MODULES:
        index=module+'/README.md'
        if path.relative_to(ROOT).as_posix()!=index and (ROOT/index).exists():nav+=f' · [Section index]({relative(path,index)})'
    return managed(text,'csf-return-navigation',nav)


def badge(label,value,color):
    width=max(160,8*(len(label)+len(value))+28);left=max(65,8*len(label)+16)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" role="img" aria-label="{html.escape(label+": "+value)}"><rect width="{width}" height="28" rx="4" fill="#{color}"/><path d="M4 0h{left-4}v28H4Q0 28 0 24V4Q0 0 4 0" fill="#29343d"/><g fill="#fff" font-family="Arial,sans-serif" font-size="12"><text x="8" y="19">{html.escape(label)}</text><text x="{left+8}" y="19">{html.escape(value)}</text></g></svg>\n'


def release_highlights(controls):
    """Show published 3.0 changes where a first-time reader can find them."""
    counts=Counter(STATUS_LABELS[c['kind']] for c in controls)
    lines=['## What changed in v3.0', '',
        'CSF 3.0 connects a news item to a score, a proposed action, a domain control, and a readiness check. You can trace why a judgment was made, repeat the assessment, and compare later results using the same method.', '',
        '**Comparison:** published 3.0 versus the recorded [pre-3.0 baseline](REPOSITORY_REVIEW.md#change-labels). These capabilities were already published in 3.0; this README update makes them easier to find.', '',
        '| Change | What changed | What you can do now |', '|---|---|---|',
        '| ![NEW in 3.0](assets/badges/change-new.svg) | [Research intake and CTSS records](research/intake/README.md) preserve individual items, sources, input reasons, and revisions. | Review each assessment and compare the declared weekly sample over time. |',
        f'| ![NEW in 3.0](assets/badges/change-new.svg) | {counts["NEW"]} research-linked controls added across all six domains. | Follow the [control catalog](resources/mitigation-catalog.md) to its research rationale, owner role, test, and failure response. |',
        f'| ![UPDATED in 3.0](assets/badges/change-updated.svg) | {counts["UPDATED"]} inherited controls refined; prior wording remains in the records. | See what changed and why before updating your local implementation. |',
        '| ![NEW in 3.0](assets/badges/change-new.svg) | [Signal tracking](research/intake/signals/README.md) links source excerpts to dispositions, proposed responsible roles, and review triggers. | Track watch items and research needs without counting every excerpt as a separate incident. |',
        '| ![UPDATED in 3.0](assets/badges/change-updated.svg) | [Readiness criteria](resources/readiness-worksheet.md) separate inherited capabilities from research extensions. | Use the [worked unit assessment](examples/unit_readiness_assessment.md) and keep missing evidence unknown. Start a new comparison when criteria change. |',
        '| ![NEW in 3.0](assets/badges/change-new.svg) | [Baseline and perspective documentation](lenses/founding-baseline-assessment.md), [schemas and agent/MCP access](integration/README.md), and linked web views. | Declare the lens behind a judgment and reuse structured records. Lens profiles remain draft templates. |',
        f'| ![RETAINED in 3.0](assets/badges/change-retained.svg) | Six domains, five causal layers, CTSS weights, and stable inherited control IDs. {counts["RETAINED"]} controls retain their inherited implementation. | Keep the core model and trace earlier records. {counts["UPDATED"]} other inherited IDs have updated guidance. |', '',
        '### Changes across the six domains', '',
        'NEW means an added control. UPDATED means a refined inherited control. RETAINED means inherited guidance. None of these labels means a new domain or taxonomy class. No controls are DEPRECATED in this comparison.', '',
        '| Domain | NEW controls | UPDATED controls | RETAINED controls |', '|---|---:|---:|---:|']
    for module,(ident,label,_) in MODULES.items():
        if not (ident.startswith('D') and ident[1:].isdigit()):continue
        domain=Counter(STATUS_LABELS[c['kind']] for c in controls if c['domain_id']==ident)
        lines.append(f'| [{label}]({module}/README.md) | {domain["NEW"]} | {domain["UPDATED"]} | {domain["RETAINED"]} |')
    lines+=['', '**Evidence limits:** more documented controls do not establish better observed readiness. Event CTSS scores remain provisional CSI judgments. See [research note 010](research/010_domain_controls_and_readiness.md) for control rationale and comparison limits.', '',
        '[Full change log](CHANGELOG.md) · [Release notes](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/CSF-3.0.0-release-notes.html) · [Remaining roadmap work](EVOLUTION.md)', '']
    return '\n'.join(lines)


def build():
    baseline=read_json(ROOT/'docs/repository-baseline.json');controls=read_json(ROOT/'resources/controls.json')
    registry=read_json(ROOT/'taxonomy/registry.json')
    schemas=list((ROOT/'schemas').glob('*.schema.json'))
    taxonomy=sum(len(rows) for rows in registry.values() if isinstance(rows,list))
    badge_specs={'version':('Framework',VERSION,'975100'),'docs-license':('Documentation','CC BY-SA 4.0','555E69'),'code-license':('Code and data','MIT','246C59'),'domains':('Scope','6 domains / 5 layers','126D87'),'controls':('Controls',str(len(controls))+' documented','975100'),'taxonomy':('Taxonomy',str(taxonomy)+' stable entries','7551A1'),'contracts':('Contracts',str(len(schemas))+' schemas','126D87'),'mapping':('UAS crosswalk','documented / not certification','555E69'),'scores':('Event CTSS','provisional judgments','820F1A')}
    for name,(label,value,color) in badge_specs.items():
        path=ROOT/'assets/badges'/f'{name}.svg';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(badge(label,value,color),encoding='utf-8',newline='\n')
    for status,color in [('NEW','246C59'),('UPDATED','126D87'),('RETAINED','555E69')]:
        (ROOT/'assets/badges'/f'change-{status.lower()}.svg').write_text(badge(status,'in 3.0',color),encoding='utf-8',newline='\n')
    for module,(ident,label,color) in MODULES.items():
        if module=='.github':continue
        ink='#101519' if color=='F6921E' else '#fff'
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 112" role="img" aria-label="{html.escape(ident+": "+label+", CSF "+VERSION)}"><rect width="900" height="112" rx="8" fill="#101519"/><rect width="12" height="112" rx="4" fill="#{color}"/><rect x="28" y="25" width="80" height="62" rx="6" fill="#{color}"/><text x="68" y="65" text-anchor="middle" font-family="Arial,sans-serif" font-size="25" fill="{ink}">{ident}</text><text x="132" y="52" font-family="Arial,sans-serif" font-size="27" fill="#f7f5ef">{html.escape(label)}</text><text x="134" y="82" font-family="Arial,sans-serif" font-size="16" fill="#bcc7ce">CSF {VERSION} | Research, controls, and evidence</text></svg>\n'
        path=ROOT/'assets/headers'/f'{module}.svg';path.parent.mkdir(exist_ok=True);path.write_text(svg,encoding='utf-8',newline='\n')
    # New indexes preserve existing section content and enumerate their actual files.
    for module in INDEX_MODULES:
        path=ROOT/module/'README.md'
        if not path.exists():path.write_text('# '+MODULES[module][1]+'\n\nUse this index to find the section’s documents, tools, and data. Source records remain data, not authorization to execute actions.\n',encoding='utf-8',newline='\n')
    for path in [p for p in files() if p.name=='README.md' and p.parent!=ROOT]:
        entries=[]
        for child in sorted(path.parent.iterdir(),key=lambda item:item.name):
            if child.is_file() and child!=path and child.suffix in {'.md','.html','.json','.py','.cjs','.svg','.png'}:
                entries.append(f'- [{child.name}]({child.name})')
            elif child.is_dir() and not child.name.startswith('.') and child.name not in {'__pycache__','node_modules'}:
                target=child.name+'/README.md' if (child/'README.md').exists() else child.name+'/'
                entries.append(f'- [{child.name}/]({target})')
        if entries:path.write_text(managed(path.read_text(encoding='utf-8'),'csf-section-files','## Section files\n\n'+'\n'.join(entries)),encoding='utf-8',newline='\n')
    root=ROOT/'README.md';text=root.read_text(encoding='utf-8')
    links={'version':baseline['framework_release']['url'],'docs-license':'LICENSE','code-license':'LICENSE','domains':'FRAMEWORK.md','controls':'resources/mitigation-catalog.md','taxonomy':'taxonomy/README.md','contracts':'schemas/README.md','mapping':'06-digital-ai-symbiosis/federal-procurement-alignment.md','scores':'research/intake/README.md'}
    header='\n'.join(f'[![{label}: {value}](assets/badges/{name}.svg)]({links[name]})' for name,(label,value,_) in badge_specs.items())
    header+='\n[![Latest CSF evidence-check workflow status](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/actions/workflows/evidence-check.yml/badge.svg)](https://github.com/CyberStrategyInstitute/cognitive-sovereignty/actions/workflows/evidence-check.yml)'
    publication=f'Framework {VERSION} is published.' if baseline['framework_release']['version']==VERSION else f'Framework {VERSION} publication is not established by the recorded {baseline["framework_release"]["version"]} release.'
    header+=f'\n\n{publication} Scope: six domains and five causal layers; {len(controls)} documented controls and {taxonomy} taxonomy entries. Code and machine-readable data: MIT. Documentation: CC BY-SA 4.0. UAS mapping is a documented crosswalk, not certification. Event CTSS values remain provisional CSI judgments. The workflow badge reports CI status, not control efficacy.\n\n[Complete page map (HTML)](https://cyberstrategyinstitute.github.io/cognitive-sovereignty/page-map.html) · [Markdown page map](PAGE_MAP.md) · [Change legend and baseline](REPOSITORY_REVIEW.md#change-labels) · [Published release]({baseline["framework_release"]["url"]})'
    # Keep the selected banner first and the existing title readable.
    if '<!-- csf-root-status:start -->' not in text:
        where=text.index('\n\n',text.index('# Cognitive Sovereignty'))
        text=text[:where]+'\n\n<!-- csf-root-status:start -->\n<!-- csf-root-status:end -->'+text[where:]
    text=managed(text,'csf-root-status',header)
    text=managed(text,'csf-release-highlights',release_highlights(controls))
    root.write_text(text,encoding='utf-8',newline='\n')
    # Create the page map itself before scanning, so coverage includes its own entry.
    map_path=ROOT/'PAGE_MAP.md'
    if not map_path.exists():map_path.write_text('# Complete CSF page map\n',encoding='utf-8',newline='\n')
    records=[]
    for path in files():
        if path.suffix=='.md':path.write_text(decorate(path,path.read_text(encoding='utf-8')),encoding='utf-8',newline='\n')
        name=path.relative_to(ROOT).as_posix();module=name.split('/')[0] if '/' in name else 'Repository'
        records.append({'id':'PAGE-'+hashlib.sha256(name.encode()).hexdigest()[:12],'path':name,'title':title(path),'module':module,'change':change(path,baseline),'status':role(path),'framework_version':VERSION,'source_owner':'Cyber Strategy Institute; cited material retains its own attribution','historical_body_preserved':historical(path)})
    grouped=defaultdict(list)
    for record in records:grouped[record['module']].append(record)
    lines=['# Complete CSF page map','',f'{len(records)} Markdown and HTML pages are listed, including section indexes, contribution templates, research notes, assessment resources, and historical reports. This map is generated from repository files. Stable PAGE IDs are derived from paths.','',f'Framework {VERSION} is published. New standards documentation in this follow-up is distinguished from changes already delivered in 3.0. [Baseline and change meanings](REPOSITORY_REVIEW.md#change-labels).','','[Search the web page map](docs/page-map.html) · [Machine-readable map](docs/page-map.json) · [Data catalog](docs/data/catalog.json)','']
    for module,rows in sorted(grouped.items()):
        lines+=['## '+module,'','| Page | Change comparison | Interpretation |','|---|---|---|']
        for r in rows:lines.append(f'| [{r["title"].replace("|","/")}]({r["path"]}) | {r["change"]} | {r["status"]} |')
        lines.append('')
    map_path.write_text(decorate(map_path,'\n'.join(lines).rstrip()+'\n'),encoding='utf-8',newline='\n')
    data={'schema_version':'1.0','framework_version':VERSION,'comparison':{k:v for k,v in baseline['comparison'].items() if k!='changes'},'source':'Repository Markdown/HTML files; generated by tools.presentation','interpretation':baseline['rules'],'count':len(records),'pages':records}
    (ROOT/'docs/page-map.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns)
    sitemap=ET.Element('{'+ns+'}urlset')
    for path in sorted((ROOT/'docs').glob('*.html')):
        entry=ET.SubElement(sitemap,'{'+ns+'}url');ET.SubElement(entry,'{'+ns+'}loc').text=baseline['framework_release']['pages_url']+('' if path.name=='index.html' else path.name)
    (ROOT/'docs/sitemap.xml').write_text(ET.tostring(sitemap,encoding='unicode')+'\n',encoding='utf-8',newline='\n')
    print(f'Built shared headers, linked badges, section indexes, and a complete {len(records)}-page map.')


def check(preserve_inputs=False):
    data=read_json(ROOT/'docs/page-map.json');actual={p.relative_to(ROOT).as_posix() for p in files()}
    indexed={r['path'] for r in data['pages']}
    if actual!=indexed or data['count']!=len(actual):raise ValueError('Page-map coverage differs from repository pages')
    if len({r['id'] for r in data['pages']})!=len(actual):raise ValueError('Page IDs must be unique')
    baseline=read_json(ROOT/'docs/repository-baseline.json')
    if preserve_inputs:
        for name,digest in baseline['presentation_input_hashes_utf8_lf'].items():
            if hashlib.sha256((ROOT/name).read_text(encoding='utf-8').encode()).hexdigest()!=digest:raise ValueError('Presentation review changed an owning assessment/control input: '+name)
        if hashlib.sha256((ROOT/'assets/CSF-Human-Control-Plane-v2.png').read_bytes()).hexdigest()!=baseline['selected_banner_sha256']:raise ValueError('Selected banner content changed')
    for path in files():
        text=path.read_text(encoding='utf-8')
        if path.suffix=='.md' and not historical(path) and '<!-- csf-return-navigation:start -->' not in text:raise ValueError('Missing return navigation: '+str(path))
    if 'assets/CSF-Human-Control-Plane-v2.png' not in (ROOT/'README.md').read_text(encoding='utf-8'):raise ValueError('Selected root banner is missing')
    for module in MODULES:
        path=ROOT/module/'README.md'
        if path.exists() and '<!-- csf-module-header:start -->' not in path.read_text(encoding='utf-8'):raise ValueError('Missing section header: '+module)
    print(f'PASS: all {len(actual)} pages are indexed; current Markdown pages have return navigation and section headers.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['build','check']);parser.add_argument('--preserve-inputs',action='store_true',help='Compare this presentation review with its recorded input hashes; not a gate on later research updates');args=parser.parse_args()
    build() if args.command=='build' else check(args.preserve_inputs)
