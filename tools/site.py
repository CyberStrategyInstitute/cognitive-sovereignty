"""Add a consistent navigation bar and style sheet to the existing static pages."""
from tools.csf import ROOT


def build():
    for name,active in [('index.html','Learn'),('csf-explorer.html','Taxonomy'),('csf-command-center.html','Command center')]:
        path=ROOT/'docs'/name;text=path.read_text(encoding='utf-8')
        if 'href="assets/site.css"' not in text:text=text.replace('</head>','<link rel="stylesheet" href="assets/site.css">\n</head>')
        if '<!-- CSF shared navigation -->' not in text:
            links=[('index.html','Learn'),('research.html','Research and scores'),('csf-explorer.html','Taxonomy'),('csf-command-center.html','Command center'),('guide.html','How to use it'),('https://github.com/CyberStrategyInstitute/cognitive-sovereignty','Repository')]
            nav='<!-- CSF shared navigation --><nav class="csf-site-nav" aria-label="Main"><strong>CSI / Cognitive Sovereignty</strong>'
            for href,label in links:nav+=f'<a href="{href}"'+(' aria-current="page"' if label==active else '')+'>'+label+'</a>'
            nav+='</nav>'
            text=text.replace('<body>','<body>\n'+nav,1)
        path.write_text(text,encoding='utf-8',newline='\n')
    # The separate legacy view links to the same reader-facing hub.
    path=ROOT/'command-center/index.html';text=path.read_text(encoding='utf-8')
    if 'href="../docs/assets/site.css"' not in text:text=text.replace('</head>','<link rel="stylesheet" href="../docs/assets/site.css">\n</head>')
    if '<!-- CSF shared navigation -->' not in text:text=text.replace('<body>','<body>\n<!-- CSF shared navigation --><nav class="csf-site-nav" aria-label="Main"><strong>CSI / Cognitive Sovereignty</strong><a href="../docs/index.html">Learn</a><a href="../docs/research.html">Research and scores</a><a href="../docs/guide.html">How to use it</a></nav>',1)
    path.write_text(text,encoding='utf-8',newline='\n')


if __name__=='__main__':build()
