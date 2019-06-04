from tkinter import *
from tkinter import ttk
import requests

HEIGHT = 500
WIDTH = 600

OPTIONS = None
with open('Currency.txt','r') as f:
	data = f.read()
	OPTIONS = data.split(',')

# print(len(OPTIONS))


def convert_currency(entry1, entry2, menu1, menu2):
	if (menu1 == menu2) or (entry1 == entry2 == '') or (menu1 == 'NONE') or (menu2 == 'NONE'):
		pass
	else:
		if entry1 == '':
			from_currency_entry.delete(0,END)
			request = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + menu2 + '&tsyms='+ menu1)
			data = request.json()
			from_currency_entry.insert(0,data[menu1])
		elif (entry1 != '' and entry2 != '') or (entry2 == ''):
			to_currency_entry.delete(0,END)
			request = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + menu1 + '&tsyms='+ menu2)
			data = request.json()
			to_currency_entry.insert(0,data[menu2])


root_window = Tk()
root_window.title('Currency Convertor')
main_frame = Frame(root_window)


left_frame = Frame(main_frame)

from_currency_entry = Entry(left_frame)
from_currency_entry.grid(row=0, column=0)

tk_var = StringVar()
from_currency_menu = ttk.Combobox(left_frame, width=10, textvar=tk_var)
from_currency_menu['values'] = OPTIONS
from_currency_menu.grid(row=1, column=0)

label = Label(left_frame, text="TO")
label.grid(column=1,row=0,rowspan=2)

left_frame.pack(side=LEFT,fill=X)


right_frame = Frame(main_frame)

to_currency_entry = Entry(right_frame)
to_currency_entry.grid(row=0, column=0)

tk_var1 = StringVar()
to_currency_menu = ttk.Combobox(right_frame, width=10, textvar=tk_var1)
to_currency_menu['values'] = OPTIONS
to_currency_menu.grid(row=1, column=0)

button = Button(right_frame, text="Convert", command=lambda: convert_currency(from_currency_entry.get().strip(), to_currency_entry.get().strip(), tk_var.get().strip(), tk_var1.get().strip()))
button.grid(column=1,row=0,rowspan=2)

right_frame.pack(side=RIGHT,fill=X)


main_frame.pack()
root_window.mainloop()