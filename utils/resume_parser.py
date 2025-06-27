from PyPDF2 import PdfReader
import docx2txt

def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return "Unsupported file format"
