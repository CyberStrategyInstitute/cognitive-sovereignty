"""Single framework version and checks for current labels, distinct from source history."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
if not re.fullmatch(r'\d+\.\d+\.\d+',VERSION):raise ValueError('VERSION must contain major.minor.patch')


def check():
    from tools.site import PAGES
    errors=[]
    for name,_ in PAGES:
        text=(ROOT/name).read_text(encoding='utf-8')
        title=re.search(r'<title>(.*?)</title>',text,re.S)
        if not title or 'v'+VERSION not in title[1]:errors.append(name+': stale page title')
        if f'<meta name="csf-version" content="{VERSION}">' not in text:errors.append(name+': stale version metadata')
        nav=re.search(r'<nav class="csf-site-nav".*?</nav>',text,re.S)
        if not nav or 'CSF v'+VERSION not in nav[0]:errors.append(name+': stale navigation version')
    for name,key in [('taxonomy/registry.json','metadata'),('docs/data/taxonomy.json','metadata')]:
        if json.loads((ROOT/name).read_text(encoding='utf-8'))[key]['version']!=VERSION:errors.append(name+': stale taxonomy version')
    if json.loads((ROOT/'docs/data/catalog.json').read_text(encoding='utf-8'))['framework_version']!=VERSION:errors.append('Stale catalog version')
    citation=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
    if f'version: "{VERSION}"' not in citation or f'Framework v{VERSION}:' not in citation:errors.append('Stale citation version')
    for name in ['README.md','FRAMEWORK.md','CHANGELOG.md','EVOLUTION.md']:
        if 'v'+VERSION not in (ROOT/name).read_text(encoding='utf-8'):errors.append(name+': missing current framework version')
    if errors:raise ValueError('\n'.join(errors))
    print(f'PASS: CSF v{VERSION} matches all seven pages, citation, current documentation, taxonomy, and data catalog.')


if __name__=='__main__':check()
