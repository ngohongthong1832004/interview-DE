#!/usr/bin/env python3
"""
Script to extract text content from PDF files
"""

import sys
try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

def read_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            print(f"PDF has {len(pdf_reader.pages)} pages")
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                print(f"Reading page {page_num}...")
                page_text = page.extract_text()
                text += f"\n--- PAGE {page_num} ---\n"
                text += page_text
                text += "\n"
            
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def save_to_text_file(text, output_path):
    """Save extracted text to a text file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to: {output_path}")
    except Exception as e:
        print(f"Error saving text: {e}")

if __name__ == "__main__":
    pdf_file = "test_data_de_devop_v2.pdf"
    output_file = "extracted_content.txt"
    
    print(f"Extracting text from: {pdf_file}")
    extracted_text = read_pdf(pdf_file)
    
    if extracted_text:
        save_to_text_file(extracted_text, output_file)
        print("\n" + "="*50)
        print("EXTRACTED CONTENT:")
        print("="*50)
        print(extracted_text[:2000] + "..." if len(extracted_text) > 2000 else extracted_text)
    else:
        print("Failed to extract text from PDF")
