import argparse
from text_extractor.pdf_extractor import extract_text_from_pdf
from text_extractor.ppt_extractor import extract_text_from_ppt
from text_extractor.utils import is_valid_file


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF or PowerPoint files.")
    parser.add_argument('--file', type=str, required=True,
                        help="Path to the PDF or PowerPoint file.")

    args = parser.parse_args()

    if not is_valid_file(args.file):
        print("Error: The file does not exist or is not accessible.")
        return

    if args.file.endswith('.pdf'):
        text = extract_text_from_pdf(args.file)
    elif args.file.endswith('.pptx'):
        text = extract_text_from_ppt(args.file)
    else:
        print("Error: Unsupported file format. Please provide a PDF or PowerPoint file.")
        return

    print(text)


if __name__ == "__main__":
    main()
