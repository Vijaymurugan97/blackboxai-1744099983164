# PDF Highlights Extractor

## Overview
This application extracts the "Table of Highlights Task/Page Description of Change Effectivity" section from PDF documents and outputs the data in a structured JSON format.

## Installation
1. Clone the repository.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the application from the command line:
```
python extractor_app.py <input_pdf> <output_json>
```

## Example
```
python extractor_app.py job1/1st-rvw-ROC-D200602000024R019.pdf output.json
