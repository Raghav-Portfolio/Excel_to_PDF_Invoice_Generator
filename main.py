import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path
#pip install openpypxl

filepaths=glob.glob('invoices/*.xlsx')
#returns a list of filepaths, where each element is the filepath of an excel file. 

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name= "Sheet 1") 
    #the sheetname argument should match the name of the sheet that's been given in the excel file 
    pdf=FPDF(orientation = 'P', unit='mm', format='A4')
    pdf.add_page()
    
    filename = Path(filepath).stem 
    # don't add ()
    invoice_number =  filename.split('-')[0]
    #grab the first item off of the list created by the split function
    date =  filename.split('-')[1]
    #grab the second item off of the list created by the split function
    
    """
    Another way of creating invoice_number and date:
    invoice_number, date = filename.split('-')
    """
    
    pdf.set_font(family='Times', size=16)
    pdf.cell(w=50, h=8, txt = f'Invoice Number {invoice_number}', ln=1)
    
    pdf.set_font(family='Times', size=16)
    pdf.cell(w=50, h=8, txt = f'date: {date}')
    pdf.output(f'PDFs/{filename}.pdf')