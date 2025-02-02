from setuptools import setup, find_packages

setup(
    name='pdf_ppt_text_extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2==3.0.0',
        'python-pptx==0.6.21',
    ],
    entry_points={
        'console_scripts': [
            'extract_text=extract_text:main',
        ],
    },
)
