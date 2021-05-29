from tkinter import *
import tkinter
from tkinter.ttk import *
import sys
sys.path.append('.\\data')
from new2 import language, theme, username
import time #thư viện thời gian #
import pyautogui # thư viện tự động bấm chuột, bấm bàn phím
import pyperclip # thư viện copy và hàm past
import speech_recognition # thư viện ghi nhận lời nói #
from googletrans import Translator # thư viện từ điển dịch của google
from keyboard import press # thư viện bấm phím trên bàn phím
import keyboard 
import os


window = Tk()
window.title("new2.py")
window.geometry("900x360")
window.resizable(0, 0)
window.config(bg='ghost white')


def EN():
	#Label
	lbl = tkinter.Label(window, text="Configure", bg="ghost white" , font=("", 20))
	lbl.place(x=380, y=0)

	tkinter.Label(window, text="Output", bg="ghost white" , font='arial 13').place(x=640, y=30)
	Output_text = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text.place(x=530, y=60)

	# tkinter.Label(window, text="Output", bg="ghost white" , font='arial 13').place(x=640, y=120)
	Output_text2 = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text2.place(x=530, y=150)

	# tkinter.Label(window, text="Output", bg="ghost white", font='arial 13').place(x=640, y=210)
	Output_text3 = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text3.place(x=530, y=240)

	Input_text=Combobox(window)
	Input_text['value'] = ("Vietnamese",
							"English",
							"Japanese")
	Input_text.current(1)
	Input_text.place(x=30, y=60)
	
	Input_text2=Combobox(window)
	Input_text2['value'] = ("Light",
							"Dark")
	Input_text2.current(0)
	Input_text2.place(x=30, y=150)

	Input_text3=tkinter.Entry(window, font='arial 10', width=20)
	Input_text3.place(x=30, y=250)

	tkinter.Label(window, text="Language", bg="ghost white", font='arial 13').place(x=90, y=25)
	tkinter.Label(window, text="Theme", bg="ghost white" , font='arial 13').place(x=100, y=115)
	tkinter.Label(window, text="Username", bg="ghost white", font='arial 13').place(x=75, y=210)

	def get_language():
		lang=Input_text.get()
		print("Language: "+ lang)
		out="Output of Read is: " + language(lang)
		Output_text.delete(1.0, END)
		Output_text.insert(END, out)

	def get_theme():
		gettheme=Input_text2.get()
		print("Theme: " + gettheme)
		out = "Output of Read is: " + theme(gettheme)
		Output_text2.delete(1.0, END)
		Output_text2.insert(END, out)

	def get_name():
		getname=Input_text3.get()
		if getname == None:
			getname = ""
		print("Username: "+ getname)
		out = "Output of Read is: " + username(getname)
		Output_text3.delete(1.0, END)
		Output_text3.insert(END, out)

	trans_btn = tkinter.Button(window, text='Get language', font='arial 12', pady=0, command=get_language, width=12, bg='royal blue1',
	                   activebackground='sky blue')
	trans_btn.place(x=230, y=50)

	trans_btn = tkinter.Button(window, text='Get theme', font='arial 12', pady=0, command=get_theme, width=12, bg='royal blue1',
	                   activebackground='sky blue')
	trans_btn.place(x=230, y=140)

	tkinter.Button(window, text='Get username', font='arial 12', pady=0, command=get_name, width=12, bg='royal blue1',
	                   activebackground='sky blue').place(x=230, y=240)


def VN():
	#Label
	lbl = tkinter.Label(window, text="Cài đặt", bg="ghost white", font=("", 20))
	lbl.place(x=380, y=0)


	tkinter.Label(window, text="Kết quả", bg="ghost white" , font='arial 13').place(x=640, y=30)
	Output_text = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text.place(x=530, y=60)

	# tkinter.Label(window, text="Kết quả", bg="ghost white", font='arial 13').place(x=640, y=120)
	Output_text2 = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text2.place(x=530, y=150)

	# tkinter.Label(window, text="Kết quả", bg="ghost white", font='arial 13').place(x=640, y=210)
	Output_text3 = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	Output_text3.place(x=530, y=240)

	Input_text2=Combobox(window)
	Input_text2['value'] = ("Sáng",
							"Tối")
	Input_text2.place(x=30, y=150)
	Input_text2.current(0)

	Input_text=Combobox(window)
	Input_text['value'] = ("Tiếng Việt",
							"Tiếng Anh",
							"Tiếng Nhật")
	Input_text.place(x=30, y=60)
	Input_text.current(1)

	# Input_text3 = Text(window, font='arial 10', height=1, wrap=WORD, padx=5, pady=5, width=30)
	# Input_text3.place(x=30, y=240)
	Input_text3=tkinter.Entry(window, font='arial 10', width=20)
	Input_text3.place(x=30, y=250)
	

	tkinter.Label(window, text="Ngôn ngữ", bg="ghost white", font='arial 13').place(x=90, y=25)
	tkinter.Label(window, text="Giao diện", bg="ghost white" , font='arial 13').place(x=100, y=115)
	tkinter.Label(window, text="Tên người dùng", bg="ghost white", font='arial 13').place(x=60, y=205)	
	
	def get_language():
		lang=Input_text.get()
		print("Ngôn ngữ: "+ lang)
		out="Kết quả ghi được: " + language(lang)
		Output_text.delete(1.0, END)
		Output_text.insert(END, out)

	def get_theme():
		gettheme=Input_text2.get()
		print("Giao diện: " + gettheme)
		out = "Kết quả ghi được là: " + theme(gettheme)
		Output_text2.delete(1.0, END)
		Output_text2.insert(END, out)

	def get_name():
		getname=Input_text3.get()
		if getname == None:
			getname = ""
		print("Tên người dùng: "+ getname)
		out = "Kết quả ghi được là: " + username(getname)
		Output_text3.delete(1.0, END)
		Output_text3.insert(END, out)


	tkinter.Button(window, text='Chọn', font='arial 12', pady=0, command=get_language, width=12, bg='royal blue1',
	                   activebackground='sky blue').place(x=230, y=50)

	tkinter.Button(window, text='Chọn', font='arial 12', pady=0, command=get_theme, width=12, bg='royal blue1',
	                   activebackground='sky blue').place(x=230, y=140)

	tkinter.Button(window, text='Chọn', font='arial 12', pady=0, command=get_name, width=12, bg='royal blue1',
	                   activebackground='sky blue').place(x=230, y=240)

os.chdir('.\\data')
submenu = Menu(window)
file = Menu(submenu, tearoff = 0) 
submenu.add_cascade(label ='File', menu = file) 
submenu.add_command(label="Vietnamese", command=VN)
submenu.add_command(label="English", command=EN)
# file.add_command(label="New window", command=openNewWindow)
# file.add_separator()
file.add_command(label ='Exit', command = window.destroy)
window.config(menu = submenu)
VN()
window.mainloop()
