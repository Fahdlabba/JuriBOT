# Arabic Legal Document Analyzer

## Overview
AI-powered tool for analyzing digitized Arabic legal documents, extracting key features relevant to specific legal cases using advanced OCR and NLP techniques.

## Features
- Arabic-optimized OCR
- ML-based text analysis
- Automated reporting
- User-friendly interface


### Prerequisites
- Python 3.7+
- Tesseract OCR
- Gemini API Key
### Quick Start

1. Clone and enter the repository:
   ```bash
   git clone git@github.com:Fahdlabba/JuriBOT.git
   cd JuriBOT
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR:
   ```bash
   sudo apt-get install tesseract-ocr
   ```
4. Verify Tesseract Installation:
   ```bash
   which tesseract
   ```
5. Install Arabic Language for Tesseract:
   ```bash
   wget https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/master/ara.traineddata
   ```
6. Move Language File to Tesseract Data Directory:
   ```bash
    sudo mv "/content/ara.traineddata" "/usr/share/tesseract-ocr/4.00/tessdata"
   ```

7. Run the Application :
   ```bash
   streamlit run main.py
   ```  