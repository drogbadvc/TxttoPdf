from fpdf import FPDF
import sys
import os
from os import listdir
from os.path import isfile, join

root_pdf = sys.argv[1]
only_files = [f for f in listdir(root_pdf) if isfile(join(root_pdf, f))]

for file in only_files:
    pdf = FPDF()

    pdf.add_font("NotoSans", style="", fname="fonts/Noto_Sans/NotoSans-Regular.ttf", uni=True)

    pdf.add_page()

    pdf.set_font("NotoSans", '', size=12)

    f = open(root_pdf + file, "r")

    file_name_path = os.path.splitext(root_pdf + file)
    file_name = os.path.basename(file_name_path[0])

    for x in f:
        pdf.multi_cell(0, 10, txt=x, align='C')

    f.close()

    pdf.output(f"pdf/{file_name}.pdf")
