
import json
import gspread
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials


json_key = json.load(open('Atcon Python-a698ebdacf53.json'))
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Atcon Python-a698ebdacf53.json', scope)
gc = pygsheets.authorize()
gc1 = gspread.authorize(credentials)
worksheet = gc.open('Test').sheet1
worksheet1 = gc1.open('AC-1 meter24.06.xls').sheet1
#worksheet.title = "Sheet1"

# for x in range(1,42):
# 	worksheet.delete_row(1)

# hr = '16'
# mins = '35'
# sec = '28'
# date = '18/6/17'
# print(date)
#srch = worksheet.find("19/6/17")
x = worksheet1.cell(3,3)
print(x.value)
#print(worksheet.get_value((2,181)))

# for x in range(0,len(srch)):
# 	row_ = srch[x].row

# 	if(get_value(2,row_) == "21")
