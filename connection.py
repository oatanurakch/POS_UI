import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load userdata from google sheet
def LoadNameUserInSheet():
    scropes = ['https://spreadsheets.google.com/auth/spreadsheets']
    cred = ServiceAccountCredentials.from_json_keyfile_name('keyCredential.json')
    file = gspread.authorize(cred)
    workbook = file.open('ListUserElectronic')
    sheet = (workbook.sheet1)
    data_get = sheet.get_all_values()
    # Change data to dictionary
    # data_get_dictform = {i[0] : i[1] for i in data_get}
    return data_get

# Update data to google sheet
def updatedata(id, mobile = '', name = ''):
    scropes = ['https://spreadsheets.google.com/auth/spreadsheets']
    cred = ServiceAccountCredentials.from_json_keyfile_name('keyCredential.json')
    file = gspread.authorize(cred)
    workbook = file.open('ListUserElectronic')
    sheet = (workbook.sheet1)
    data_get = sheet.get_all_values()
    # update value
    cell = 1
    for i in data_get:
        if i[0] == id:
            # If mobile not equal to default argument
            if mobile != '':    
                sheet.update_cell(cell, 3, mobile)
            # If name not equal to default argument
            if name != '':
                sheet.update_cell(cell, 2, name)
        cell += 1
    


if __name__ == '__main__':
    allvalue = LoadNameUserInSheet()
    print(allvalue[0])
    # updatedata(id = 'D6500450', mobile = '0986565856', name = 'อนุรักษ์ ชูศรี')
    