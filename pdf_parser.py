import logging
import pdfplumber

# Set up logger
logger = logging.getLogger('pdf_parser')

def extract_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
            return full_text
    except Exception as e:
        logger.error(f"Failed to extract text from {pdf_path}: {e}")
        raise
