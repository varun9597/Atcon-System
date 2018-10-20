from tkinter import *
from tkinter import ttk
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def calculate():
	json_key = json.load(open('Atcon Python-a698ebdacf53.json'))
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('Atcon Python-a698ebdacf53.json', scope)
	gc = gspread.authorize(credentials)
	worksheet = gc.open('AC-1 meter24.06.xls').sheet1

	Range1 = range_entry.get()
	range2 = worksheet.range(Range1)
	
	
	for x in range(0,len(range2)):
		s = range2[x]	
		text.insert(INSERT,s.value + '\n')



root = Tk()
root.title("Atcon Python")

text = Text(root)

range_entry = Entry(root)
range_entry.pack()
range_entry.focus_set()

b = Button(root, text="Submit", command=calculate)
text.pack()
b.pack()

root.bind('<Return>', calculate)
#pprint(response)
root.mainloop()

