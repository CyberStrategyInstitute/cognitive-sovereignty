import unittest
import subprocess
import sys
from unittest.mock import patch
import xml.etree.ElementTree as ET
from tools.csf import ROOT,read_json
from tools.check_repo import markdown_anchors
from tools.presentation import build,check,files,MODULES,release_highlights
from tools.query import query
from tools.version import VERSION


class PresentationTests(unittest.TestCase):
    def test_documented_standalone_check_command_keeps_working(self):
        result=subprocess.run([sys.executable,'tools/csf.py','check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(0,result.returncode,result.stderr)

    def test_every_document_is_discoverable_including_templates_and_history(self):
        check()
        data=read_json(ROOT/'docs/page-map.json')
        self.assertEqual({p.relative_to(ROOT).as_posix() for p in files()},{r['path'] for r in data['pages']})
        self.assertIn('.github/PULL_REQUEST_TEMPLATE.md',{r['path'] for r in data['pages']})
        self.assertTrue(any(r['historical_body_preserved'] for r in data['pages']))

    def test_presentation_generator_never_writes_owning_assessments_or_banner(self):
        baseline=read_json(ROOT/'docs/repository-baseline.json')
        protected={ROOT/path for path in baseline['presentation_input_hashes_utf8_lf']}|{ROOT/'assets/CSF-Human-Control-Plane-v2.png'}
        with patch('pathlib.Path.write_text',autospec=True,return_value=1) as write:
            build()
        self.assertFalse(protected & {call.args[0] for call in write.call_args_list})

    def test_domain_headers_have_distinct_colors_and_textual_change_counts(self):
        colors=[];controls=read_json(ROOT/'resources/controls.json')
        for folder,(ident,label,color) in MODULES.items():
            if not (ident.startswith('D') and ident[1:].isdigit()):continue
            colors.append(color)
            image=ET.parse(ROOT/'assets/headers'/f'{folder}.svg').getroot()
            self.assertEqual('img',image.attrib['role']);self.assertIn(label,image.attrib['aria-label'])
            text=(ROOT/folder/'README.md').read_text(encoding='utf-8')
            self.assertIn('Control comparison:',text)
            self.assertIn(str(sum(c['domain_id']==ident and c['kind']=='added' for c in controls))+' NEW',text)
        self.assertEqual(6,len(set(colors)))

    def test_markdown_anchors_handle_duplicate_headings_links_and_explicit_ids(self):
        text='# A **clear** [title](https://example.org)\n## Repeat\n## Repeat\n<a id="M-004"></a>\n```\n# Ignore this\n```\n'
        anchors=markdown_anchors(text)
        self.assertIn('a-clear-title',anchors);self.assertIn('repeat-1',anchors);self.assertIn('M-004',anchors);self.assertNotIn('ignore-this',anchors)

    def test_page_discovery_is_bounded_and_retains_interpretation(self):
        result=query('pages',text='readiness',limit=2)
        self.assertEqual(2,len(result['results']));self.assertTrue(result['next_offset'])
        self.assertTrue(all(row['path'] and row['status'] and row['framework_version']==VERSION for row in result['results']))

    def test_root_preserves_star_history_and_separates_license_and_mapping_claims(self):
        text=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertIn('FRAMEWORK.md#star-history',text)
        star=text.split('## Star History',1)[1]
        self.assertIn('<picture>',star)
        self.assertIn('<img src="https://api.star-history.com/svg?repos=CyberStrategyInstitute/cognitive-sovereignty',star)
        self.assertIn('prefers-color-scheme: dark',star)
        self.assertIn('Open the interactive chart',star)
        self.assertIn('Code and machine-readable data: MIT',text)
        self.assertIn('not certification',text)
        self.assertIn('api.star-history.com',(ROOT/'FRAMEWORK.md').read_text(encoding='utf-8'))

    def test_release_highlights_use_owning_control_counts(self):
        controls=read_json(ROOT/'resources/controls.json')
        text=release_highlights(controls)
        self.assertIn(text,(ROOT/'README.md').read_text(encoding='utf-8'))
        self.assertIn('already published in 3.0',text)
        for label in ['NEW','UPDATED','RETAINED']:
            self.assertIn(f'![{label} in 3.0]',text)
        # A changed input must change the summary, rather than leave stale numbers.
        sample=[{'kind':'added','domain_id':'D1'},{'kind':'inherited','domain_id':'D1'}]
        generated=release_highlights(sample)
        self.assertIn('| [Biological](01-biological/README.md) | 1 | 0 | 1 |',generated)

    def test_sitemap_covers_the_actual_pages_directory(self):
        links={node.text for node in ET.parse(ROOT/'docs/sitemap.xml').getroot().iter() if node.tag.endswith('}loc')}
        base=read_json(ROOT/'docs/repository-baseline.json')['framework_release']['pages_url']
        expected={base+('' if p.name=='index.html' else p.name) for p in (ROOT/'docs').glob('*.html')}
        self.assertEqual(expected,links)

    def test_stale_publication_claims_are_removed_without_erasing_research_proposals(self):
        for name in ['README.md','CHANGELOG.md','RECOMMENDATIONS.md','IMPLEMENTATION.md','monitoring/README.md']:
            text=(ROOT/name).read_text(encoding='utf-8')
            self.assertNotIn('before merging this PR',text)
            self.assertNotIn('once the included GitHub workflow is merged',text)
        self.assertIn('proposed',(ROOT/'research/008_operator_objectives_and_persuasion.md').read_text(encoding='utf-8'))
