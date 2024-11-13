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
