# PDF and PPT Text Extractor

A command-line tool to extract text from PDF and PowerPoint (PPTX) files. Built with Python, this tool is designed to be simple, efficient, and easy to use.

---

## Features

- Extract text from PDF files.
- Extract text from PowerPoint (PPTX) files.
- Command-line interface powered by `argparse`.
- Modular and extensible codebase.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Moh-Gebril/PDF-PPT-Text-Extractor.git
   cd PDF-PPT-Text-Extractor
   ```

## Setup

### Setting Up the Virtual Environment and Installing Dependencies

```bash
make install
```

### (Optional) Install the Tool Globally

```bash
make build
python setup.py install
```

## Usage

### Command-Line Interface

To extract text from a file, run:

```bash
python extract_text.py --file <file_path>
```

#### Example:

```bash
python extract_text.py --file tests/samples/sample.pdf
```

### Supported File Formats

- **PDF** (.pdf)
- **PowerPoint** (.pptx)

## Project Structure

```
PDF-PPT-Text-Extractor/
├── text_extractor/          # Core text extraction logic
│   ├── __init__.py
|   ├── samples/                 # Sample files for testing
│   |   ├── sample.pdf
│   |   └── sample.pptx│
|   ├── pdf_extractor.py     # PDF text extraction
│   ├── ppt_extractor.py     # PPT text extraction
│   └── utils.py             # Utility functions
├── tests/                   # Unit tests
│   ├── __init__.py
│   ├── test_pdf_extractor.py
│   └── test_ppt_extractor.py
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
├── setup.py                 # Installation script
├── extract_text.py          # CLI entry point
└── Makefile                 # Build and test automation
```

## Development

### Setting Up the Virtual Environment

The Makefile automatically creates and activates a virtual environment for you. Run the following command to set up the environment and install dependencies:

```bash
make install
```

### Running Tests

To run the unit tests, use:

```bash
make test
```

### Building the Project

To build the project, use:

```bash
make build
```

### Cleaning Up

To remove build artifacts, temporary files, and the virtual environment, use:

```bash
make clean
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **PyPDF2** for PDF text extraction.
- **python-pptx** for PowerPoint text extraction.

## Authors
Mohamed Gebril
