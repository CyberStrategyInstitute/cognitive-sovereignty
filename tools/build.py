"""Rebuild derived files from canonical data. No collection or publication."""
from tools.csf import ROOT, generated_outputs, read_json
from tools.event_monitor import build as reports
from tools.export import outputs
from tools.signals import build as signals
from tools.site import build as site
from tools.controls import build as controls
from tools.presentation import build as presentation


def main():
    controls()
    for path,text in generated_outputs(read_json(ROOT/'taxonomy/registry.json')).items():path.write_text(text,encoding='utf-8',newline='\n')
    reports(read_json(ROOT/'research/intake/events.json'))
    signals(read_json(ROOT/'research/intake/signals/register.json'))
    presentation()
    for path,text in outputs().items():path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8',newline='\n')
    site()
    print('Built scores, reports, signal views, catalog, site data, and navigation.')


if __name__=='__main__':main()
