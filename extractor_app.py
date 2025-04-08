import argparse
import json
import logging
from pdf_parser import extract_text
from data_extractor import extract_highlights
from logger import setup_logger

# Set up logger
logger = setup_logger()

def main(input_pdf, output_json):
    try:
        # Extract text from PDF
        full_text = extract_text(input_pdf)
        logger.info(f"Extracted text from {input_pdf}")

        # Extract highlights
        highlights = extract_highlights(full_text)
        logger.info("Highlights extracted successfully")

        # Write to JSON file
        with open(output_json, 'w') as json_file:
            json.dump(highlights, json_file, indent=4)
        logger.info(f"Output written to {output_json}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract highlights from PDF.")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_json", help="Path to the output JSON file")
    args = parser.parse_args()
    
    main(args.input_pdf, args.output_json)
