import PySimpleGUI as sg
import os
import sys
sys.path.append('.\\data')
from new3 import language, theme, username

sg.theme('LightGreen')
sg.set_options(element_padding=(0, 0))

def second_window():
	menu_def = [['&Tệp', ['&Thông tin', 'E&xit']],
                ['&Chỉnh sửa', ['&Ngôn ngữ', ['Tiếng Việt', 'Tiếng Anh', ], ], ],
                ['&Giúp đỡ', '&Về chúng tôi...'], ]
	right_click_menu = ['Unused', ['Phải', '!&Nhấp', '&Menu', 'E&xit', 'Thông tin']]
	layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
		  [sg.Text("Ngôn ngữ", size=(25,1)),sg.Text("Kết quả")],
		  [sg.Combo(["Tiếng Anh", "Tiếng Việt"], default_value = "Tiếng Anh", key='-INPUT4-', size=(27,1)),sg.Text(size=(20,1), key='-OUTPUT4-')],
		  [sg.Text("Giao diện", size=(25,1)),sg.Text("Kết quả")],
		  [sg.Combo(["Tối","Sáng"], default_value = "Sáng", key='-INPUT5-', size=(27,1)),sg.Text(size=(20,1), key='-OUTPUT5-')],
		  [sg.Text("Tên người dùng", size=(25,1)),sg.Text("Kết quả")],
		  [sg.Input(default_text = "Admin", size=(21,1), key='-INPUT6-'),sg.Button("Chọn"),sg.Text(size=(20,1), key='-OUTPUT6-')]]
	window = sg.Window("Cài đặt",
					layout,
					default_element_size=(12, 1),
					default_button_element_size=(12, 1),
					right_click_menu=right_click_menu)
	event, values = window.read()
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Exit':
			break

		if event == 'Về chúng tôi...':
			window.disappear()
			sg.popup('Thông tin về chương trình', 'Phiên bản 1.0',
					'Phiên bản PySimpleGUI', sg.version,  grab_anywhere=True)
			window.reappear()
		elif event == 'Thông tin':
			second_window()
		elif event == 'Tiếng Anh':
			window.close()
			first_window()
		elif event == "Chọn":
			window['-OUTPUT4-'].update(values['-INPUT4-'],text_color="yellow")
			window['-OUTPUT5-'].update(values['-INPUT5-'],text_color="yellow")
			window['-OUTPUT6-'].update(values['-INPUT6-'],text_color="yellow")

		language(values['-INPUT4-'])
		theme(values['-INPUT5-'])
		username(values['-INPUT6-'])

	window.close()

def first_window():
	menu_def = [['&File', ['&Properties', 'E&xit']],
	                ['&Edit', ['&Language', ['Vietnamese', 'English', ], ], ],
	                ['&Help', '&About...'], ]

	right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

	layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
			  [sg.Text("Language", size=(25,1)),sg.Text("Final")],
			  [sg.Combo(["English", "Vietnamese"], default_value = "English", key='-INPUT1-', size=(27,1)),sg.Text(size=(20,1), key='-OUTPUT1-')],
			  [sg.Text("Theme", size=(25,1)),sg.Text("Final")],
			  [sg.Combo(["Dark","Light"], default_value = "Light", key='-INPUT2-', size=(27,1)),sg.Text(size=(20,1), key='-OUTPUT2-')],
			  [sg.Text("Username", size=(25,1)),sg.Text("Final")],
			  [sg.Input(default_text = "Admin", size=(21,1), key='-INPUT3-'),sg.Button("Select"),sg.Text(size=(20,1), key='-OUTPUT3-')]]

	window = sg.Window('Setting',
	                   layout,
	                   default_element_size=(12, 1),
	                   default_button_element_size=(12, 1),
	                   right_click_menu=right_click_menu)
	
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Exit':
			break

		if event == 'About...':
			window.disappear()
			sg.popup('About this program', 'Version 1.0',
					'PySimpleGUI Version', sg.version,  grab_anywhere=True)
			window.reappear()
		elif event == 'Open':
			filename = sg.popup_get_file('file to open', no_window=True)
			print(filename)
		elif event == 'Properties':
			second_window()
		elif event == 'Vietnamese':
			window.close()
			second_window()
		elif event == "Select":
			window['-OUTPUT1-'].update(values['-INPUT1-'],text_color="yellow")
			window['-OUTPUT2-'].update(values['-INPUT2-'],text_color="yellow")
			window['-OUTPUT3-'].update(values['-INPUT3-'],text_color="yellow")


		language(values['-INPUT1-'])
		theme(values['-INPUT2-'])
		username(values['-INPUT3-'])

	window.close()

os.chdir('.\\data\\data')
first_window()