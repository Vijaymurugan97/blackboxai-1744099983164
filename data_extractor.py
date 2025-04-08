import re
import json
import logging

# Set up logger
logger = logging.getLogger('data_extractor')

def extract_highlights(full_text):
    highlights = {}
    try:
        # Regex to find the section
        pattern = r'Table of Highlights Task/Page Description of Change Effectivity(.*?)(?=\n\n|\Z)'
        match = re.search(pattern, full_text, re.DOTALL)
        
        if match:
            section_text = match.group(1)
            # Further processing to structure the data
            lines = section_text.strip().split('\n')
            for line in lines:
                # Example processing logic
                key_value = line.split(':', 1)
                if len(key_value) == 2:
                    highlights[key_value[0].strip()] = key_value[1].strip()
        else:
            logger.warning("No highlights section found.")
        
        return highlights
    except Exception as e:
        logger.error(f"Error extracting highlights: {e}")
        raise
