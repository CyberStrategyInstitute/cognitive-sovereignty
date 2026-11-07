"""Build shared navigation, brand assets, and domain practice entrypoints."""
import re
from tools.csf import ROOT,read_json

PAGES=[('docs/index.html','Learn'),('docs/csf-explorer.html','Taxonomy'),('docs/csf-command-center.html','Command center'),('docs/research.html','Research and scores'),('docs/guide.html','How to use it'),('docs/practice.html','Controls and readiness'),('command-center/index.html','Command center')]

def navigation(active,prefix):
    links=[('index.html','Learn'),('research.html','Research and scores'),('csf-explorer.html','Taxonomy'),('practice.html','Controls and readiness'),('csf-command-center.html','Command center'),('guide.html','How to use it')]
    nav='<nav class="csf-site-nav" aria-label="Main"><a class="csf-brand" href="'+prefix+'index.html"><img src="'+prefix+'assets/brand/csi-shield-white-orange.svg" width="32" height="48" alt="Cyber Strategy Institute shield"><span>CSI / Cognitive Sovereignty</span></a>'
    for href,label in links:nav+='<a href="'+prefix+href+'"'+(' aria-current="page"' if label==active else '')+'>'+label+'</a>'
    return nav+'<a href="https://github.com/CyberStrategyInstitute/cognitive-sovereignty">Repository</a></nav>'

def summary(prefix):
    controls=read_json(ROOT/'resources/controls.json')
    retained=sum(c['kind']!='added' for c in controls);refined=sum(c['kind']=='refined' for c in controls);added=sum(c['kind']=='added' for c in controls)
    return '<!-- CSF practice summary:start --><section class="csf-practice-summary" aria-label="Domain controls and readiness"><h2>From research to tested capability</h2><p>'+str(retained)+' inherited controls retained, '+str(refined)+' refined, and '+str(added)+' added. Readiness is unknown until a scoped assessment supplies results.</p><nav class="jump" aria-label="Practice resources"><a href="'+prefix+'practice.html#domains">Six domains</a><a href="'+prefix+'practice.html#controls">Control catalog</a><a href="'+prefix+'practice.html#resources">Assessment resources</a><a href="'+prefix+'practice.html#roadmap">Roadmap status</a></nav><div data-domain-summary></div></section><!-- CSF practice summary:end -->'

def build():
    for name,active in PAGES:
        path=ROOT/name;text=path.read_text(encoding='utf-8');prefix='../docs/' if name.startswith('command-center/') else ''
        text=re.sub(r'<nav class="csf-site-nav".*?</nav>',lambda _:navigation(active,prefix),text,flags=re.S)
        if 'assets/site.css' not in text:text=text.replace('</head>','<link rel="stylesheet" href="'+prefix+'assets/site.css">\n</head>')
        if 'assets/practice.js' not in text:text=text.replace('</head>','<script src="'+prefix+'assets/practice.js" defer></script>\n</head>')
        if name in {'docs/index.html','docs/csf-explorer.html','docs/csf-command-center.html','command-center/index.html'}:
            block=summary(prefix)
            if '<!-- CSF practice summary:start -->' in text:text=re.sub(r'<!-- CSF practice summary:start -->.*?<!-- CSF practice summary:end -->',lambda _:block,text,flags=re.S)
            else:
                marker='<!-- IV. EVOLUTION -->' if name=='docs/index.html' else '<div class="layout">' if 'explorer' in name else '</header>'
                text=text.replace(marker,(block+'\n'+marker) if marker!='</header>' else marker+'\n'+block,1)
        text=re.sub(r'<svg([^>]*)>\s*<use href="#cseal"\s*/>\s*</svg>',lambda m:'<img class="csf-shield" src="'+prefix+'assets/brand/csi-shield-white-orange.svg" alt="CSI shield" '+('width="260" height="260"' if '260' in m[1] else 'width="42" height="54"')+'>',text)
        from collections import Counter
        from tools.csf import tier,score
        counts=Counter(tier(score(r['ctss'])) for r in read_json(ROOT/'taxonomy/registry.json')['manipulation_techniques'])
        for key,label in [('critical','Critical ≥80'),('high','High 70–79'),('elevated','Elevated 60–69')]:
            text=re.sub(re.escape(label)+r' — \d+ Techniques',lambda _:label+' — '+str(counts[key])+' Techniques',text)
        text=text.replace('Command Center · v2.0','Command Center · v2.1.0').replace('Command Center — v2.0','Command Center · v2.1.0')
        path.write_text(text,encoding='utf-8',newline='\n')

if __name__=='__main__':build()
