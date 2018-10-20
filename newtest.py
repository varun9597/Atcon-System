import json
from pathlib import Path
import os.path
import gspread
import pygsheets
from os import path
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from tkinter import ttk

kwh=0
ir=0

def main_part(*args):

	json_key = json.load(open('Atcon Python-1dd56d750dc9.json'))
	scope = ['https://spreadsheets.google.com/feeds',
		     'https://www.googleapis.com/auth/drive',
       		 'https://www.googleapis.com/auth/spreadsheets']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('Atcon Python-1dd56d750dc9.json', scope)
	gc = pygsheets.authorize()
	gc1 = gspread.authorize(credentials)
	worksheet = gc.open('AC-1 meter24.06.xls').sheet1
	worksheet1 = gc1.open('AC-1 meter24.06.xls').sheet1


#date_value = "19/6/17"
	date_value = date.get() #get is used for getting value from tkinter
	#print(date_value)

#time_value = "8:56:33"
	time_value = time1.get()
	time_value2 = time2.get()
	#print(time_value)
	#array = time_value.split(":")

	cell=worksheet.find(time_value)
	cell2=worksheet.find(time_value2)
	req_value = cell[0].row    #kwh value of corresspondong row
	req_value2 = cell2[0].row

	kwh1 = worksheet1.cell(req_value,21).value
	kwh2 = worksheet1.cell(req_value2,21).value
	
	kwh_value = (float)(kwh2) - (float)(kwh1)

	kwh.set(round(kwh_value,2)) #set is used for setting value for tkinter label
	array = time_value.split(":")
	array2 = time_value2.split(":")
	hrs_value = (((int)(array2[0])*60)+(int)(array2[1])-((int)(array[0])*60)+(int)(array[1]))/60
	hrs.set(round(hrs_value,1))
	phkwh.set(round((kwh_value/hrs_value),2))

	# print(kwh)
	# print(ir)




root = Tk()
root.title("Atcon Python")

mainframe = ttk.Frame(root, padding = " 3 3 12 12")
mainframe.grid(column=0,row=0, sticky = (N,W,E,S))
mainframe.columnconfigure(0, weight =1)
mainframe.rowconfigure(0, weight=1)

date = StringVar()
time2 = StringVar()
kwh = StringVar()
time1 = StringVar()
hrs = StringVar()
phkwh = StringVar()

ttk.Label(mainframe,text="Date:").grid(column=1,row=1,sticky=(W,E))
date_entry = ttk.Entry(mainframe, width = 7, textvariable = date)
date_entry.grid(column=2,row=1,sticky=(W,E))

ttk.Label(mainframe,text="Start Time:").grid(column=1,row=2,sticky=(W,E))
time_entry = ttk.Entry(mainframe, width = 7, textvariable = time1)
time_entry.grid(column=2,row=2,sticky=(W,E))

ttk.Label(mainframe,text="End Time:").grid(column=1,row=3,sticky=(W,E))
time_entry2 = ttk.Entry(mainframe, width = 7, textvariable = time2)
time_entry2.grid(column=2,row=3,sticky=(W,E))


ttk.Label(mainframe,text="kwh Consumed:").grid(column=3,row=1,sticky=(W,E))
ttk.Label(mainframe, textvariable=kwh).grid(column=4,row=1, sticky=(W,E))



ttk.Label(mainframe,text="Hours:").grid(column=3,row=2,sticky=(W,E))
ttk.Label(mainframe, textvariable=hrs).grid(column=4,row=2, sticky=(W,E))

ttk.Label(mainframe,text="Per Hour Kwh:").grid(column=3,row=3,sticky=(W,E))
ttk.Label(mainframe, textvariable=phkwh).grid(column=4,row=3, sticky=(W,E))


ttk.Button(mainframe, text = "Fetch",command = main_part).grid(column=2,row = 4, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

date_entry.focus()
time_entry.focus()

root.bind('<Return>',main_part)


root.mainloop()
