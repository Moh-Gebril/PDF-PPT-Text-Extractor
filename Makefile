# Makefile for PDF and PPT Text Extractor

# Variables
PYTHON = python3
PIP = pip3
VENV = venv
ACTIVATE = . $(VENV)/bin/activate
PROJECT_NAME = pdf_ppt_text_extractor
TEST_DIR = tests

# Default target
all: venv install test

# Create a virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

# Install dependencies
install: venv
	@echo "Installing dependencies..."
	$(ACTIVATE) && $(PIP) install -r requirements.txt
	@echo "Dependencies installed."

# Run tests
test: install
	@echo "Running tests..."
	$(ACTIVATE) && $(PYTHON) -m unittest discover -v -s $(TEST_DIR)
	@echo "Tests completed."

# Clean up build artifacts and virtual environment
clean:
	@echo "Cleaning up..."
	rm -rf build dist *.egg-info $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Cleanup complete."

# Build the project
build: install
	@echo "Building the project..."
	$(ACTIVATE) && $(PYTHON) setup.py sdist bdist_wheel
	@echo "Build complete."

# Upload to PyPI (if applicable)
upload: build
	@echo "Uploading to PyPI..."
	$(ACTIVATE) && twine upload dist/*
	@echo "Upload complete."

# Run the tool
run: install
	@echo "Running the tool..."
	$(ACTIVATE) && $(PYTHON) extract_text.py --file samples/sample.pdf
	@echo "Execution complete."

# Help command
help:
	@echo "Available commands:"
	@echo "  make venv         - Create a virtual environment"
	@echo "  make install      - Install dependencies"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean up build artifacts and virtual environment"
	@echo "  make build        - Build the project"
	@echo "  make upload       - Upload to PyPI (requires twine)"
	@echo "  make run          - Run the tool with a sample PDF"
	@echo "  make help         - Show this help message"

.PHONY: all venv install test clean build upload run help