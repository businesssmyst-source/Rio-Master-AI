import fitz  # This is PyMuPDF
from PIL import Image
import os

def read_pdf(file_path):
    """Rio extracts all text from a PDF and reports page count."""
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' was not found, Founder."
        
    try:
        doc = fitz.open(file_path)
        page_count = len(doc)
        text = ""
        
        # Rio loops through every page to gather knowledge
        for page_num in range(page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        doc.close()
        
        if not text.strip():
            return f"This PDF has {page_count} pages, but it appears to be scanned images only. No selectable text found."
            
        return f"Document Analyzed ({page_count} pages): \n\n" + text
        
    except Exception as e:
        return f"Rio System Error reading PDF: {str(e)}"

def read_image_info(image_path):
    """Rio analyzes image dimensions, format, and color profiles."""
    if not os.path.exists(image_path):
        return f"Error: Image '{image_path}' not found."
        
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            img_format = img.format
            mode = img.mode  # Checks if it is RGB, CMYK, etc.
            
            return (f"Image Analysis Complete, Boss:\n"
                    f"- Name: {os.path.basename(image_path)}\n"
                    f"- Format: {img_format}\n"
                    f"- Dimensions: {width}x{height} pixels\n"
                    f"- Color Profile: {mode}")
    except Exception as e:
        return f"Rio System Error reading Image: {str(e)}"