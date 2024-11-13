# PDF to Image Converter

A simple Python application that converts PDF files into images using a GUI built with `tkinter`. The program allows users to select a PDF file, convert it to individual JPEG images, and saves the images in a designated folder on the desktop.

## Features
- **PDF Conversion**: Converts each page of a PDF to a JPEG image.
- **File Selection**: Allows the user to select a PDF file via a file dialog.
- **Progress Bar**: Displays the progress of the conversion.
- **Desktop Folder**: Saves images in an `extracted_images` folder created on the desktop.

## Requirements
Make sure you have the following installed:

- Python 3.6 or higher
- Required Python packages:
  - `pdf2image`
  - `Pillow`
  - `tkinter` (included in the standard Python library)
  - `poppler` (needs to be installed separately; see below)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Paulina-Palma/pdf_to_jpg_converter.git
```

### 2. Install dependencies
Use pip to install the required Python packages:
```bash
pip install pdf2image Pillow PyInstaller
```

### 3. Install Poppler
pdf2image requires Poppler, a PDF rendering library. Follow the instructions below based on your operating system:

**Windows**

- Download Poppler from Poppler for Windows.
- Extract the ZIP file to a directory (e.g., C:\poppler-xx).
- Add the bin directory to your system's PATH:
- Go to System Properties -> Environment Variables.
- Add C:\poppler-xx\bin to the PATH variable.

**macOS**

Install Poppler using Homebrew:
```bash
brew install poppler
```

**Linux**

Install Poppler using your package manager (e.g., Ubuntu):
```bash
sudo apt update
sudo apt install poppler-utils
```

## Usage

Running the Standalone Application:

- Run the standalone executable:

**On Windows**: Double-click pdf_to_image_converter.exe.

**On macOS/Linux**: Execute the file in a terminal.

Running from Source

- Run the script using Python:
python pdf_to_image_converter.py

- Use the GUI to:

Browse and select a PDF file.
Click the "Convert" button to start the conversion.
View the progress bar indicating conversion status.
Images will be saved to the extracted_images folder on your desktop.

## Screenshots

## Troubleshooting

Error: "Unable to get page count. Is poppler installed and in PATH?"
Make sure Poppler is correctly installed and added to your system's PATH.

