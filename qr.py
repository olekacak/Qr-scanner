import cv2
from pyzbar.pyzbar import decode
from pdf2image import convert_from_path
import numpy as np
import webbrowser

pdf_path = "C:\\Users\\Ole Kacak\\Desktop\\Python Project\\qr scanner\\assets\\sample.pdf"

def scan_qr_from_pdf(pdf_path):
    # Convert PDF to images
    pages = convert_from_path(pdf_path, dpi=300)
    opened_urls = set()  # Set to keep track of already opened URLs
    
    for i, page in enumerate(pages):
        # Convert PIL image to a NumPy array for OpenCV
        img = np.array(page)
        
        # Convert RGB to BGR (OpenCV uses BGR format)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # Decode the QR code
        qr_codes = decode(img)
        
        if qr_codes:
            for qr_code in qr_codes:
                data = qr_code.data.decode('utf-8')
                print(f"QR Code Data (Page {i+1}): {data}")
                
                # Check if the data is a URL and hasn't been opened yet
                if data.startswith("http://") or data.startswith("https://"):
                    if data not in opened_urls:
                        webbrowser.open(data)  
                        opened_urls.add(data)  
                else:
                    print(f"Scanned QR code on Page {i+1} is not a URL.")
        else:
            print(f"No QR code found on Page {i+1}.")

scan_qr_from_pdf(pdf_path)
