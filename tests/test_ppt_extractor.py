import unittest
import os
from text_extractor.ppt_extractor import extract_text_from_ppt


class TestPptExtractor(unittest.TestCase):
    def test_extract_text_from_ppt(self):
        # Path to the sample PowerPoint file
        sample_ppt_path = os.path.join(
            os.path.dirname(__file__), "samples/sample.pptx")

        # Check if the file exists
        self.assertTrue(os.path.exists(sample_ppt_path),
                        f"Sample PPT file not found at {sample_ppt_path}")

        # Extract text from the sample PowerPoint file
        text = extract_text_from_ppt(sample_ppt_path)

        # Assert that the extracted text is a non-empty string
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

        # Check if the output contains delimiters and headers
        self.assertIn("---", text)  # Check for delimiters
        self.assertIn("Header:", text)  # Check for headers


if __name__ == "__main__":
    unittest.main()
