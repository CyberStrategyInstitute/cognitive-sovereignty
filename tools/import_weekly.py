"""Import the supplied CSF collection without changing the originals."""
import argparse
import hashlib
import json
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = {"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main", "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")


def source_document(path):
    with zipfile.ZipFile(path) as z:
        relations = {e.attrib["Id"]:e.attrib for e in ET.fromstring(z.read("word/_rels/document.xml.rels"))}
        root = ET.fromstring(z.read("word/document.xml"))
        paragraphs = []
        for i,p in enumerate(root.findall(".//w:p",NS)):
            text = "".join(t.text or "" for t in p.findall(".//w:t",NS))
            urls = []
            for link in p.findall(".//w:hyperlink",NS):
                rel = relations.get(link.attrib.get("{"+NS["r"]+"}id"),{})
                if rel.get("TargetMode")=="External": urls.append(rel["Target"])
            paragraphs.append({"index":i,"text":text,"urls":list(dict.fromkeys(urls))})
        extra = {}
        for name in z.namelist():
            if re.match(r"word/(footnotes|endnotes|comments|header\d+|footer\d+)\.xml$",name):
                node=ET.fromstring(z.read(name))
                extra[name]=["".join(t.text or "" for t in p.findall(".//w:t",NS)) for p in node.findall(".//w:p",NS)]
        media=[n for n in z.namelist() if n.startswith("word/media/")]
        external_images=[r["Target"] for r in relations.values() if "image" in r.get("Type","") and r.get("TargetMode")=="External"]
        return {"paragraphs":paragraphs,"other_parts":extra,"embedded_media":media,"external_images":external_images,"external_links":[r["Target"] for r in relations.values() if r.get("TargetMode")=="External"]}


def parse_ranked(document, source_id, week_ends):
    active=False; week=-1; blocks=[]; current=None
    stop=re.compile(r"^(Three most consequential|Recommended framework actions|Framework actions|Proposed framework changes|Competing and disconfirming|Emerging indicators|Source.quality|Bottom line)",re.I)
    for p in document["paragraphs"]:
        text=p["text"]
        if text.startswith("Top 12 developments"):
            active=True; week+=1; current=None
            continue
        if active and stop.match(text): active=False; current=None
        match=re.match(r"^(\d{1,2})\.\s+(.+)",text)
        if active and match and 1<=int(match[1])<=12:
            current={"source_id":source_id,"week_end":week_ends[week],"rank":int(match[1]),"title":match[2],"paragraphs":[]}
            blocks.append(current)
        if active and current: current["paragraphs"].append(p)
    return blocks


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source",type=Path)
    parser.add_argument("--archive",type=Path,required=True,help="Local archive outside the public checkout")
    args=parser.parse_args()
    manifest=[]; blocks=[]; signals=[]
    endings={
        "Cognitive Sovereignty Friday Brief Sep - 23 Oct 26.docx":["2026-09-21","2026-09-25","2026-10-02","2026-10-09","2026-10-16"],
        "Cognitive Sovereignty Friday Brief.docx":["2026-10-30"],
        "Cognitive Sovereignty Framework Friday Brief.docx":["2026-11-06"]}
    for i,path in enumerate(sorted(p for p in args.source.rglob("*") if p.is_file()),1):
        relative=path.relative_to(args.source).as_posix()
        source_id="DOC-"+hashlib.sha256(relative.encode('utf-8')).hexdigest()[:12]
        raw=path.read_bytes(); dest=args.archive/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists() and dest.read_bytes()!=raw: raise ValueError("Archive conflict; preserve previous version: "+relative)
        if not dest.exists(): shutil.copyfile(path,dest)
        record={"source_id":source_id,"relative_path":relative,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"original_unchanged":True}
        if path.suffix.lower()==".docx":
            document=source_document(path)
            dump(ROOT/"research/intake/raw"/(source_id+".json"),document)
            current=parse_ranked(document,source_id,endings[path.name]); blocks+=current
            record.update(paragraphs=len(document["paragraphs"]),ranked_occurrences=len(current),embedded_images=len(document["embedded_media"]),external_images=len(document["external_images"]))
            # Preserve lower-salience watchlists as signals, not fabricated news events.
            section=None; week=None
            for p in document["paragraphs"]:
                text=p["text"]
                if text.startswith(("Review period:","Review window:")): week=text
                if text in {"Investigate","Monitor","Emerging indicators to watch","Emerging indicators","Recommended framework actions","Framework actions","Adopt now"}: section=text; continue
                if text.startswith(("Competing and disconfirming","Source-quality","Bottom line","Cognitive Sovereignty Friday","Top 12")): section=None
                if section and text and len(text)<2000:
                    signals.append({"source_id":source_id,"paragraph":p["index"],"section":section,"week_context":week,"text":text,"record_type":"watch_or_action_signal"})
        else:
            # Keep metadata and unranked context in the local archive, not just selected excerpts.
            record["text_archived"]=True
        manifest.append(record)
    # Markdown editions contain additional evidence and different editorial selections.
    aliases={
        ("2026-10-30",1):("2026-10-30",1), ("2026-10-30",2):("2026-10-30",3),
        ("2026-10-30",3):("2026-10-30",2), ("2026-10-30",4):("2026-10-30",4),
        ("2026-11-06",3):("2026-11-06",2)}
    for rec in manifest:
        if not rec["relative_path"].endswith("_brief.md"): continue
        text=(args.source/rec["relative_path"]).read_text(encoding="utf-8-sig")
        week=re.search(r"2026-\d\d-\d\d",rec["relative_path"])[0]
        matches=list(re.finditer(r"^### (\d+)\. (.+)$",text,re.M))
        for n,match in enumerate(matches):
            end=matches[n+1].start() if n+1<len(matches) else len(text)
            body=text[match.start():end].split("\n## ")[0]
            rank=int(match[1]); alias=aliases.get((week,rank))
            blocks.append({"source_id":rec["source_id"],"week_end":week,"rank":rank,"title":match[2],"alias":list(alias) if alias else None,"paragraphs":[{"index":None,"text":body,"urls":re.findall(r"\]\((https?://[^)]+)\)",body)}]})
        # Explicitly preserve the unranked Fan Perspective as its own context item.
        if week=="2026-11-06":
            para=next((p for p in text.split("\n\n") if "metacognitive Perspective" in p),None)
            if para: blocks.append({"source_id":rec["source_id"],"week_end":week,"rank":15,"title":"A metacognitive approach to learning and performance in human-AI interaction","record_type":"context","paragraphs":[{"index":None,"text":para,"urls":re.findall(r"\]\((https?://[^)]+)\)",para)}]})
    dump(ROOT/"research/intake/manifest.json",{"imported_on":"2026-11-07","files":manifest,"coverage_gaps":["No October 16-23 ranked edition found, despite the compilation filename.","Source selection was already curated; uncollected minor world events cannot be reconstructed from these files."]})
    dump(ROOT/"research/intake/occurrences.json",blocks)
    dump(ROOT/"research/intake/signals.json",signals)
    print(f"Archived {len(manifest)} files; extracted {len(blocks)} item occurrences and {len(signals)} watch/action signals.")
    for b in blocks:
        if b.get("alias"): continue
        print(b["week_end"],b["rank"],b["title"])


if __name__=="__main__": main()
