from fpdf import FPDF

lista = ["s","jola","s","xd"]

pdf = FPDF(orientation='P', unit = 'mm', format='A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)


c=0
for i in lista:
    pdf.cell(40, 10, lista[c])
    c+=1

pdf.add_page()

pdf.output('tuto1.pdf', 'F')

