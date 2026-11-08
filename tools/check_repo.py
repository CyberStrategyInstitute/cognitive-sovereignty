"""Check local document links and HTML anchors without network requests."""
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from tools.csf import ROOT
from tools.presentation import files
import html


def markdown_anchors(text):
    text=re.sub(r'```.*?```|~~~.*?~~~','',text,flags=re.S)
    parser=Links();parser.feed(text);ids=set(parser.ids);counts={}
    for heading in re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$',text,re.M):
        heading=re.sub(r'!?\[([^\]]+)\]\([^)]*\)',r'\1',heading)
        heading=html.unescape(re.sub(r'<[^>]*>','',heading)).replace('`','')
        slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
        suffix=counts.get(slug,0);counts[slug]=suffix+1
        ids.add(slug+(f'-{suffix}' if suffix else ''))
    return ids

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if 'id' in values:self.ids.add(values['id'])
        for key in ('href','src'):
            if values.get(key):self.links.append(values[key])

def check():
    errors=[]; count=0; anchor_cache={}
    paths=files()
    for path in paths:
        text=path.read_text(encoding='utf-8')
        if path.suffix=='.html':
            parser=Links();parser.feed(text);links=parser.links
        else:
            text=re.sub(r'```.*?```','',text,flags=re.S)
            links=[m[0] or m[1] for m in re.findall(r'\]\((?:<([^>]+)>|([^\s)]+))(?:\s+"[^"]*")?\)',text)]
            parser=Links();parser.feed(text);links+=parser.links
            links += re.findall(r'^\[[^\]]+\]:\s*<?([^\s>]+)>?',text,re.M)
        for link in links:
            url=urlsplit(link)
            if url.scheme or url.netloc or not url.path and not url.fragment:continue
            target=(path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT.resolve()):errors.append(f'{path.relative_to(ROOT)}: link leaves repository {link}');continue
            if not target.exists():errors.append(f'{path.relative_to(ROOT)}: missing {link}');continue
            if url.fragment and target.suffix=='.html':
                other=Links();other.feed(target.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in other.ids:errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
            if url.fragment and target.suffix=='.md':
                if target not in anchor_cache:anchor_cache[target]=markdown_anchors(target.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in anchor_cache[target]:errors.append(f'{path.relative_to(ROOT)}: missing Markdown anchor {link}')
            count+=1
    if errors:raise ValueError('\n'.join(errors))
    print(f'PASS: {count} local document links and Markdown/HTML anchors resolve.')

if __name__=='__main__':check()
