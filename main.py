import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit='mm', format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    pdf.set_font("Times", size=16, style='B')

    # Use the variable invoice_nr instead of the string "invoice_nr."
    pdf.cell(w=50, h=8, text=f"invoice_nr-{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf", "F")

# Save or display the PDFs as needed
# For example:

