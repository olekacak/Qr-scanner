
# QR Code Scanner from PDF (Python)

This Python script scans and decodes QR codes embedded in a PDF file. If a QR code contains a URL, it will automatically open it in your default web browser.

## 📦 Requirements

- Python 3.7 or higher
- [Poppler](http://blog.alivate.com.au/poppler-windows/) (required for `pdf2image` to work)
- Python packages:
  - opencv-python
  - pyzbar
  - pdf2image
  - numpy

## ⚙️ Installation

1. **Clone the repository or download the files.**

2. **Install the required Python packages**  
   Run this command in your terminal or command prompt to install dependencies from the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

3. **Install Poppler**
   - **Windows**:  
     Download from [this link](http://blog.alivate.com.au/poppler-windows/), extract it, and add the `bin` folder to your system’s PATH.
   - **macOS**:  
     Use Homebrew:
     ```
     brew install poppler
     ```

## 🚀 Usage

1. Open the script and update the PDF path:
   ```python
   pdf_path = "C:\Users\YourName\Path\To\yourfile.pdf"
   ```

2. Run the script:
   ```
   python your_script_name.py
   ```

3. The script will:
   - Convert each page of the PDF into an image
   - Detect QR codes on each page
   - Print the decoded data to the terminal
   - Automatically open any URLs found in your browser

## ✅ Example Output

```
QR Code Data (Page 1): https://example.com
QR Code Data (Page 2): Hello World
Scanned QR code on Page 2 is not a URL.
No QR code found on Page 3.
```

## 📌 Notes

- Best results are achieved with clear and high-resolution PDFs (300 DPI recommended).
- If QR codes are too small or blurry, they may not be detected.

## 🧾 License

MIT License

Copyright (c) 2025 Amier Roslan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
