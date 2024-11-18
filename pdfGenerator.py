from fpdf import FPDF

# Creating a new PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", "", 12)

# New content for health and physiotherapy development environments and technologies
content_health = """
Teste
"""

# Adding content to the new PDF
pdf.multi_cell(0, 10, content_health)

# Saving the new PDF file
pdf_output_path_health = "C:/Users/valen/OneDrive/Desktop/pdfGenerator/Teste.pdf"
pdf.output(pdf_output_path_health)