import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path
#pip install openpypxl

filepaths=glob.glob('invoices/*.xlsx')
#returns a list of filepaths, where each element is the filepath of an excel file. 

for filepath in filepaths:
     
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
    pdf.cell(w=50, h=8, txt = f'Invoice Number {invoice_number}', ln=2)
    
    pdf.set_font(family='Times', size=16)
    pdf.cell(w=50, h=8, txt = f'Date: {date}', ln = 1)
    
    df = pd.read_excel(filepath, sheet_name= "Sheet 1")
    
    #Add a header
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(90,90,90)
    pdf.cell(w=28, h=8, txt=columns[0], border=1)
    pdf.cell(w=45, h=8, txt=columns[1], border=1)
    pdf.cell(w=45, h=8, txt=columns[2], border=1)
    pdf.cell(w=40, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    
   
    
    #Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=8)
        pdf.set_text_color(90,90,90)
        pdf.cell(w=28, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=45, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=45, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border =1, ln=1)
    
    
    
    
    
    pdf.output(f'PDFs/{filename}.pdf')