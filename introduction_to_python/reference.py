import numpy as np
import json


# Function to extract the required text into matrix
def ExtractText(response):
    documentResults = response['analyzeResult']['pageResults']
    Vendor = ''
    Date = ''
    all_table = []
    Final_Matrix = []
    next_cell_date = ''
    for page in documentResults:
        tables = page['tables']
        previous = 0
        for table in tables:
            Matrix = [[np.nan for i in range(table['columns'])] for j in range(table['rows'])]
            for cell in table['cells']:
                
                Matrix[cell['rowIndex']][cell['columnIndex']] = cell['text']
            Final_Matrix.append(Matrix)      
    return( (Final_Matrix))




with open('C:/Users/Vasista/Desktop/datadecodeai/lineExtraction/Freezex/FreezexJsonResponse.json') as f:
  response = json.load(f)

data = ExtractText(response)
print(data)



"""
#Function to extract Invoice level Details
DocumentDetails = response['analyzeResult']['documentResults'][0]['fields']
def GetInvoiceDetails(DocumentDetails): 
    Result = {} 
    keys = DocumentDetails.keys() 
    tax = 0 
    without_tax = 0 
    total = 0 
    overdue = 0 
    if("Invoice_Date" in keys): 
        try: 
            Result['Invoice_Date'] = DocumentDetails['Invoice_Date']['text'] 
        except: 
            Result['Invoice_Date'] = '' 
    
    if("Vendor_ABN" in keys): 
        try: 
            Result['Vendor_ABN'] = DocumentDetails['Vendor_ABN']['valueString'] 
        except: 
            Result['Vendor_ABN'] = '' 
    if("Sub_Total" in keys): 
        try: 
            Result['Sub_Total'] = DocumentDetails['Sub_Total']['valueNumber'] 
        except: 
            Result['Sub_Total'] = 0 
    if("Account_Number" in keys): 
        try: 
            Result['Account_Number'] = DocumentDetails['Account_Number']['valueString'] 
        except: 
            Result['Account_Number'] = '' 
    if("Vendor" in keys): 
        try: 
            Result['Vendor'] = DocumentDetails['Vendor']['valueString'] 
        except: 
            Result['Vendor'] = '' 
    if("Invoice_Amount" in keys): 
        try: 
            Result['Invoice_Total'] = DocumentDetails['Invoice_Amount']['valueNumber'] 
        except: 
            Result['Invoice_Total'] = 0 
    if("GST" in keys): 
        try: 
            Result['GST'] = DocumentDetails['GST']['valueNumber'] 
        except: 
            Result['GST'] = 0 
    if("Invoice_Number" in keys): 
        try: 
            Result['Invoice_Number'] = DocumentDetails['Invoice_Number']['valueString'] 
        except: 
            Result['Invoice_Number'] = '' 
    if("Due_Date" in keys): 
        try: 
            Result['Due_Date'] = DocumentDetails['Due_Date']['text'] 
        except: 
            Result['Due_Date'] = '' 
    if("PO_Number" in keys): 
        try: 
            Result['PO_Number'] = DocumentDetails['PO_Number']['valueString'] 
        except: 
            Result['PO_Number'] = '' 
    if("To_Address" in keys): 
        try: 
            Result['To_Address'] = DocumentDetails['To_Address']['valueString'] 
        except: 
            Result['To_Address'] = '' 
    if("Ship_Address" in keys): 
        try: 
            Result['Ship_Address'] = DocumentDetails['Ship_Address']['valueString'] 
        except: 
            Result['Ship_Address'] = '' 
    if("CO_Number" in keys): 
        try: 
            Result['CO_Number'] = DocumentDetails['CO_Number']['valueString'] 
        except: 
            Result['CO_Number'] = '' 
    if("Order_Date" in keys): 
        try: 
            Result['Order_Date'] = DocumentDetails['Invoice_Number']['text'] 
        except: 
            Result['Order_Date'] = '' 
    if("Del_Docket" in keys): 
        try: 
            Result['Del_Docket'] = DocumentDetails['Del_Docket']['valueString'] 
        except: 
            Result['Del_Docket'] = '' 
    if("Customer_ABN" in keys): 
        try: 
            Result['Customer_ABN'] = DocumentDetails['Customer_ABN']['valueString'] 
        except: 
            Result['Customer_ABN'] = '' 
    
    
    return(Result)
    """