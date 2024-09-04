
# PDF to Audio Converter

This Python script converts the text from a PDF file into an audio file (MP3 format). It uses `PyPDF2` to extract text from the PDF, `gTTS` (Google Text-to-Speech) to convert the text into speech, and `Tkinter` to select the PDF file through a simple graphical interface.

## How to Use

1. Run the script.
2. A file dialog will appear—select the PDF file you want to convert.
3. The script processes the PDF and generates an MP3 file with the same name as the PDF in the same directory.

## Requirements

Install the required Python packages with:

```bash
pip install PyPDF2 gTTS tqdm tkinter
