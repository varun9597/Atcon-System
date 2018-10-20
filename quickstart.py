


from tkinter import *
from tkinter import ttk
from pprint import pprint
from oauth2client import file
from googleapiclient import discovery


def calculate():
	global range_entry
	global response
	credentials = file.Storage('credentials.json').get()
	service = discovery.build('sheets', 'v4', credentials=credentials)
	spreadsheet_id = '1_1-KYepdzZV2xApxGcNNxroF9fp42b3Y8zt6fT-tb-Y'  # TODO: Update placeholder value.

	value_render_option = ''  # TODO: Update placeholder value.

	date_time_render_option = ''  # TODO: Update placeholder value.

	Range1 = range_entry.get()
	request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=Range1)
	response = request.execute()
	text.insert(INSERT,response.get('values'))


root = Tk()
root.title("Atcon Python")
#mainframe = ttk.Frame(root,padding =  "3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
#mainframe.columnconfigure(0, weight = 1)
#mainframe.rowconfigure(0, weight = 1)
text = Text(root)

range_entry = Entry(root)
range_entry.pack()
range_entry.focus_set()
#range_entry = ttk.Entry(mainframe, width = 10, textvariable=Range1)
#range_ = ''  # TODO: Update placeholder value.
b = Button(root, text="Submit", command=calculate)
text.pack()
b.pack()




#ttk.Label(mainframe, text = response)


root.bind('<Return>', calculate)
#pprint(response)
root.mainloop()