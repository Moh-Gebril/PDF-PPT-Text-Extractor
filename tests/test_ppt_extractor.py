import unittest
from text_extractor.ppt_extractor import extract_text_from_ppt


class TestPptExtractor(unittest.TestCase):
    def test_extract_text_from_ppt(self):
        text = extract_text_from_ppt('tests/samples/sample.pptx')
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)


if __name__ == '__main__':
    unittest.main()
