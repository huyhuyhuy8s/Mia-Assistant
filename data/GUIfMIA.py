#Thư viện python của developer
from tkinter import *
import tkinter
from tkinter.ttk import *
# from new2 import language, theme, username
import time #thư viện thời gian #
import pyautogui # thư viện tự động bấm chuột, bấm bàn phím
import pyperclip # thư viện copy và hàm past
import speech_recognition # thư viện ghi nhận lời nói #
from googletrans import Translator # thư viện từ điển dịch của google
from keyboard import press # thư viện bấm phím trên bàn phím
import keyboard 
import os
import Mia
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import pyaudio
import os
from datetime import datetime
from datetime import date
import wikipedia
import webbrowser
import time
import os
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from Color_Console import *
import math
from youtube_search import YoutubeSearch
import sys
sys.path.append('.\\data')
import new2
from users_compare import users_compare
from Mia import *

mia_ear = sr.Recognizer()
mia_mouth = pyttsx3.init()
mia_brain = ""

window = Tk()
window.title("GUIfMIA.py")
window.geometry("1280x600")
window.resizable(0, 0)
window.config(bg='ghost white')
canvas = Canvas(window, width=1280, height=600, background='ghost white')

lbl = tkinter.Label(window, text="Input", bg="ghost white" , font=("", 15))
lbl.place(x=180, y=20)

lbl2 = tkinter.Label(window, text="Output", bg="ghost white" , font=("", 15))
lbl2.place(x=530, y=20)

lbl3 = tkinter.Label(window, text="Thông báo", bg="ghost white" , font=("", 15))
lbl3.place(x=860, y=20)

Input_text = Text(window, font='arial 10', height=23, wrap=WORD, padx=5, pady=5, width=35)
Input_text.place(x=50, y=50)

Output_text = Text(window, font='arial 10', height=23, wrap=WORD, padx=5, pady=5, width=35)
Output_text.place(x=400, y=50) 

Output_text = Text(window, font='arial 10', height=23, wrap=WORD, padx=5, pady=5, width=35)
Output_text.place(x=750, y=50) 

ok=False
os.system('cls' if os.name=='nt' else 'clear')
os.chdir('.\\data')
# Ngôn ngữ người dùng
while ok == False:
	file1 = open("language.txt","r+")
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		new.language()
	else:
		l=file1.read()
		if "EN" in l or "en" in l or "En" in l or "eN" in l:
			print("Using language: " + l)
		else:
			print("Ngôn ngữ đang sử dụng: " + l)
		ok=True

#Nhập tên người dùng
while ok == True:
	file1 = open("username.txt","r+")
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		new.username()
	else:
		username=file1.read()
		if "EN" in l or "en" in l or "En" in l or "eN" in l:
			print("User's name: " + username)
		else:
			print("Tên người dùng: " + username)
		ok=False

#Nhập giao diện người dùng
while ok == False:
	#Nhập giao diện người dùng
	file1 = open("theme.txt","r+")
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		new.theme()
	else:
		theme=file1.read()
		if "EN" in l or "en" in l or "En" in l or "eN" in l:
			print("Using theme: " + theme)
		else:
			print("Giao diện đang sử dụng: " + theme)
		ok=True


def VNmain(username):
	# Các biến số ban đầu
	mia_ear = sr.Recognizer()
	mia_mouth = pyttsx3.init()
	mia_brain = ""

	# Get default audio device using PyCAW
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))

	loichao=VN_time(username)
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	o=0 
	stopai=0

	while True:
		with sr.Microphone() as mic:
			mia_brain="Đang chờ lệnh!"
			Output_text.insert(END, "Mia: " + mia_brain)
			# audio = mia_ear.listen(mic)
			audio = mia_ear.listen(mic,timeout=10, phrase_time_limit=10)
		try:
			you = mia_ear.recognize_google(audio)
		except:
			you = ""
		print("You: " + you)
		
		if "Hi Mia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you or "Chào Mia" in you:
			o=2

			if thoigian >= 23 or thoigian <= 3: #Ngủ đei
				ans = VN_doyouwanttosleep()
				if "có" in ans or "Có" in ans:
					VNshutdown()
					break
				else:
					VN_cont()

			mia_brain = loichao + ", Mình là Mia. Bạn cần gì?" 
			print("Mia: ",mia_brain)
			noi(gTTS(mia_brain,lang='vi',slow=False))

			#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
			while stopai<3:
				# Get current volume 
				currentVolumeDb = volume.GetMasterVolumeLevel()
				currentVol=currentVolumeDb
				volume.SetMasterVolumeLevel(-28, None)
				currentVolumeDb2 = volume.GetMasterVolumeLevel()
				times=currentVolumeDb - currentVolumeDb2
				volume.SetMasterVolumeLevel(currentVolumeDb, None)
				with sr.Microphone() as mic:
					mia_brain = "Mình đang nghe đây"
					print("Mia: ",mia_brain)
					noi(gTTS(mia_brain,lang='vi',slow=False))
					# audio = mia_ear.listen(mic)
					while currentVolumeDb>=currentVolumeDb2:
						currentVolumeDb=currentVolumeDb - 1
						volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
					while currentVolumeDb<=currentVol:
						currentVolumeDb=currentVolumeDb + 1
						volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					print("Mia: ...")
				try:
					you = mia_ear.recognize_google(audio, language="vi-VN")
				except:
					if stopai == 2:
						you=input("Nhập câu lệnh: ")
					else:
						stopai=stopai+1
						VN_tryagain()
						continue		
			
				print("You: " + you)

				if you != '':
					mia_brain = VN_compare(you,username,loichao)
					if mia_brain == None:
						mia_brain = users_compare(you,username,loichao)
						if mia_brain == None:
							print(f"Mia: Bạn có thể xem qua các kết quả tìm kiếm của {you}\n" + str('"https://www.google.com/search?&q="' + you.replace(" ","%20")))
							mia_brain="Xin lỗi! Mình chưa được dạy về nó, hãy thử lại nhé."
				else:
					VN_tryagain()
					continue

				if mia_brain == 2:
					break
				elif mia_brain == 1:
					continue
				else:
					print("Mia: "+ str(mia_brain))
					noi(gTTS(mia_brain,lang='vi',slow=False))


# tkinter.Button(window, text='Chọn', font='arial 12', pady=0, command=ai, width=12, bg='royal blue1',
#                    activebackground='sky blue').place(x=138, y=540)

if "EN" in l or "en" in l or "En" in l or "eN" in l:
	EN(username)
	pass
else:
	VNmain(username)
	pass

# os.chdir('.\\data')`
submenu = Menu(window)
file = Menu(submenu, tearoff = 0) 
submenu.add_cascade(label ='File', menu = file) 
# submenu.add_command(label="Vietnamese", command=VN)
# submenu.add_command(label="English", command=EN)
# file.add_command(label="New window", command=openNewWindow)
# file.add_separator()
file.add_command(label ='Exit', command = window.destroy)
window.config(menu = submenu)

window.mainloop()