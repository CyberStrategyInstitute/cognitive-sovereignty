"""Check local document links and HTML anchors without network requests."""
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from tools.csf import ROOT

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if 'id' in values:self.ids.add(values['id'])
        for key in ('href','src'):
            if values.get(key):self.links.append(values[key])

def check():
    errors=[]; count=0
    paths=[p for p in ROOT.rglob('*') if p.suffix in {'.md','.html'} and not any(x.startswith('.') for x in p.relative_to(ROOT).parts)]
    for path in paths:
        text=path.read_text(encoding='utf-8')
        if path.suffix=='.html':
            parser=Links();parser.feed(text);links=parser.links
        else:
            text=re.sub(r'```.*?```','',text,flags=re.S)
            links=[m[0] or m[1] for m in re.findall(r'\]\((?:<([^>]+)>|([^\s)]+))(?:\s+"[^"]*")?\)',text)]
        for link in links:
            url=urlsplit(link)
            if url.scheme or url.netloc or not url.path and not url.fragment:continue
            target=(path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT.resolve()):continue
            if not target.exists():errors.append(f'{path.relative_to(ROOT)}: missing {link}');continue
            if url.fragment and target.suffix=='.html':
                other=Links();other.feed(target.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in other.ids:errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
            count+=1
    if errors:raise ValueError('\n'.join(errors))
    print(f'PASS: {count} local document links and HTML anchors resolve.')

if __name__=='__main__':check()
