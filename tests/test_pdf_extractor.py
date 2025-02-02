import unittest
from text_extractor.pdf_extractor import extract_text_from_pdf


class TestPdfExtractor(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        text = extract_text_from_pdf('tests/samples/sample.pdf')
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)


if __name__ == '__main__':
    unittest.main()
