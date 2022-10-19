import pandas as pd
import os
import json
import requests as r
URL_company = 'https://www.northdata.com/_api/company/v1/company'
URL_person = 'https://www.northdata.com/_api/person/v1/person'

file = 'Seznam1.xlsx'
x=pd.ExcelFile(file)
df=x.parse('Germany')

py_list_Name=df['Name'].tolist()
N=len(py_list_Name)

py_list_District=df['District Court'].tolist()
py_list_registerId=df['registered number'].tolist()
py_list_if_company=df['Company'].tolist()
py_list_date_of_birth=df['Birthday'].tolist()

for i in range(N):
    if py_list_if_company[i]=='company':
        params = {
            'name': py_list_Name[i],
            'address': py_list_District[i],
            #'registerId': py_list_registerId[i]
            #'registerCity': py_list_District[i],
            'events': 'true',
            'eventTypes': 'YearlyReport|AddressChange|CapitalChange|ControlChange|Insolvency|InsolvencyChange|LegalFormChange|Liquidation|NameChange|NewCompany|OtherChange|RegisterChange|StatutoryChange|Termination|ManagementChange',
            'history': 'true',   #historical data
            'financials': 'true',   #financial performance indicators
            'sheets': 'true',     #sheets (balance sheet, earnings)
            'mktgtech': 'true',    # mktg & tech performance indicators
            'relations':'true', #related company and person data
            'extras': 'true',   #phone, fax number, email adress, url, vatID
            'api_key': '####-####'
            }
        URL = URL_company
    else:
        params = {
            'firstName': py_list_Name[i].split()[0],
            'lastName': py_list_Name[i].split()[1],
            'address': py_list_District[i],
            'birthDate': py_list_date_of_birth[i],
            'events': 'true',
            'eventTypes': 'YearlyReport|AddressChange|CapitalChange|ControlChange|Insolvency|InsolvencyChange|LegalFormChange|Liquidation|NameChange|NewCompany|OtherChange|RegisterChange|StatutoryChange|Termination|ManagementChange',
            'history': 'true',   #historical data
            'sheets': 'true',
            'financials': 'true',   #financial performance indicators
            'mktgtech': 'true',    # mktg & tech performance indicators
            'relations':'true', #related company and person data
            'extras': 'true',   #phone, fax number, email adress, url, vatID
            'api_key': '####-####'
        }
        URL = URL_person
       
    resp = r.get(URL, params=params)
    with open(f'output_{py_list_Name[i]}.txt', 'w') as outfile:
        json.dump(resp.json(), outfile)
