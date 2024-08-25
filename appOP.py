import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
from tqdm import tqdm

# Función para abrir el diálogo de selección de archivo
def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Seleccionar archivo PDF"
    )
    return file_path

# Función para convertir el texto a audio y guardar como .mp3
def pdf_to_audio(pdf_path, output_file):
    with open(pdf_path, 'rb') as path:
        pdf_reader = PyPDF2.PdfReader(path)
        full_text = ""
        for page_num in tqdm(range(len(pdf_reader.pages)), desc="Procesando páginas del PDF"):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                print(f"\nLeyendo página {page_num + 1}:\n")
                print(text)
                full_text += text

        # Convertir el texto a audio usando gTTS
        tts = gTTS(text=full_text, lang='es')  # Puedes cambiar el idioma a 'en' para inglés
        tts.save(output_file)
        print(f"Audio guardado como {output_file}")

if __name__ == "__main__":
    # Seleccionar el archivo PDF
    pdf_path = select_pdf_file()

    if pdf_path:
        # Crear el archivo de audio
        output_file = pdf_path.replace('.pdf', '.mp3')
        pdf_to_audio(pdf_path, output_file)
    else:
        print("No se seleccionó ningún archivo.")
