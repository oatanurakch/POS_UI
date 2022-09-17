import gspread
from oauth2client.service_account import ServiceAccountCredentials

scropes = ['https://spreadsheets.google.com/auth/spreadsheets']
cred = ServiceAccountCredentials.from_json_keyfile_name('keyCredential.json')

file = gspread.authorize(cred)
workbook = file.open('ListUserElectronic')
sheet = workbook.sheet1
print(sheet.range('A1:B2'))