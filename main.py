import pandas as pd
import glob 
#pip install openpypxl

filepaths=glob.glob('invoices/*.xlsx')
#returns a list of filepaths, where each element is the filepath of an excel file. 

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name= "Sheet 1") 
    #the sheetname argument should match the name of the sheet that's been given in the excel file 
    print(df)