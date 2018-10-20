#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pathlib import Path
import os.path
import gspread
import pygsheets
from os import path
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from tkinter ttk

def main_part():
	json_key = json.load(open('Atcon Python-a698ebdacf53.json'))
	scope = ['https://spreadsheets.google.com/feeds',
    	     'https://www.googleapis.com/auth/drive',
        	 'https://www.googleapis.com/auth/spreadsheets']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('Atcon Python-a698ebdacf53.json', scope)
	gc = pygsheets.authorize()
	gc1 = gspread.authorize(credentials)
	worksheet = gc.open('AC-1 meter24.06.xls').sheet1
	worksheet1 = gc1.open('AC-1 meter24.06.xls').sheet1



	# worksheet.title = "Sheet1"
	if path.exists("new.txt"):
		pass

	else:
		f = open("new.txt","w+")
		if worksheet1.cell(1,1).value != 'No. ':
			for x in range(1,42):
				worksheet1.delete_row(1)

	# hr = '16'
	# mins = '36'
	# sec = '35'
	# date = '18/6/17'
	print("Enter Date\n")
	date = input()
	print("Enter Time\n")
	time = input()

	srch = worksheet.find(date)
	# x = worksheet1.cell(180,3)
	# print(x.value)
	# print(worksheet.get_value((2,181)))
	date_start = srch[0].row
	date_end = srch[-1].row
	date_diff = date_end - date_start

	print(date_start)
	print(date_end)

	mid_row = (int)((date_start + date_end)/2)
	mid_row_value = worksheet1.cell(mid_row,3).value

	print(mid_row_value)

	mid_row_hr = mid_row_value[:2]

	print(mid_row_hr)

	if mid_row_hr > time[:2]:
		for x in range(date_start,mid_row+1):
			if worksheet1.cell(x,3).value == time:
				print("kWh : "+worksheet1.cell(x,21).value)
				print("Ir : "+worksheet1.cell(x,7).value)

	elif mid_row_hr < time[:2]:
		for y in range(mid_row,date_end + 1):
			if worksheet1.cell(y,3).value == time:
				print("kWh : "+worksheet1.cell(y,21).value)
				print("Ir : "+worksheet1.cell(y,7).value)

	else:
		print("kWh : "+worksheet1.cell(mid_row,21).value)
		print("Ir : "+worksheet1.cell(mid_row,7).value)

root = Tk()
root.title("Atcon Python")
mainframe = ttk.Frame(root,padding =  "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
text = Text(root)

