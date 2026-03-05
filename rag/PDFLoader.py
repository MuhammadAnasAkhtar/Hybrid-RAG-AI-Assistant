import os
import fitz
from rag.Config import PDF_FOLDER

def load_pdfs():
    documents = []

    if not os.path.exists(PDF_FOLDER):
        return documents

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(PDF_FOLDER, file))
            text = ""
            for page in doc:
                text += page.get_text()
            documents.append(text)

    return documents