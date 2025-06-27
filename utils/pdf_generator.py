from fpdf import FPDF
from io import BytesIO

def create_pdf_resume(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()
