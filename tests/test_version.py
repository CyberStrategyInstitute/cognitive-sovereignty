import unittest
from tools.version import check


class FrameworkVersionTests(unittest.TestCase):
    def test_all_current_version_labels_match_the_single_source(self):
        check()
