import time #thư viện thời gian #
from tkinter import * # thư viện giao diện #
import pyautogui # thư viện tự động bấm chuột, bấm bàn phím
import pyperclip # thư viện copy và hàm past
import speech_recognition # thư viện ghi nhận lời nói #
from googletrans import Translator # thư viện từ điển dịch của google
from keyboard import press # thư viện bấm phím trên bàn phím
import keyboard 

# keyboard.press_and_release('enter') = dichthuat

# tạo bảng giao diện và tên
root = Tk()
# kích thước bảng (dài x rộng)
root.geometry('900x240')
root.resizable(0, 0)
root.config(bg='ghost white')
# tên ứng dụng
root.title("Dịch tiếng VN <=> EN Hahuto")

# tạo nhãn "Tiếng Việt"
Label(root, text="Tiếng Việt", font='arial 13 bold', bg='white smoke').place(x=200, y=10)
# tạo khung nhập 
Input_text = Text(root, font='arial 15', height=6, wrap=WORD, padx=5, pady=5, width=30)
# vị trí khung nhập
Input_text.place(x=30, y=40)

# tạo nhãn "English"
Label(root, text="English", font='arial 13 bold', bg='white smoke').place(x=680, y=10)
# tạo khung xuất nội dung
Output_text = Text(root, font='arial 15', height=6, wrap=WORD, padx=5, pady=5, width=30)
# ví trí khung xuất nội dung
Output_text.place(x=530, y=40)

# hàm dịch thuật
def dichthuat():
  # khai báo và gáng biến
    translator = Translator()
    # dịch từ tiếng Anh sang tiếng Việt
    anhviet = translator.translate(text=Input_text.get(1.0, END))
    # Dịch từ tiếng Việt sang tiếng Anh
    vietanh = translator.translate(text=Input_text.get(1.0, END), scr='en', dest='vi')
    a = anhviet.src
    # print("Ngôn ngữ nhập vào là: ", b)

    # nếu phát hiện ngôn ngữ nhập là "en" thì in ra kết quả dịch Việt sang Anh
    if a == "en":
        # xóa nội dung cũ trong khung xuất nội dung
        Output_text.delete(1.0, END)
        # xuất kết quả ra tring khung nội dung 
        Output_text.insert(END, vietanh.text)
        # tự dộng copy 
        pyperclip.copy(vietanh.text)
        # print("Tiếng anh là: ", vietanh.text)

    # nếu phát hiện ngôn ngữ nhập là "vi" thì in ra kết quả dịch là Anh sang Việt    
    else:
        #
        Output_text.delete(1.0, END)
        Output_text.insert(END, anhviet.text)
        pyperclip.copy(anhviet.text)
        # print(" Tiếng việt là: ", anhviet.text)


# nút xóa nội dung
def xoa():
    # xóa nội dung nhập
    Input_text.delete(1.0, END)
    # xóa nội dung xuất
    Output_text.delete(1.0, END)


# nhạp liệu bằng giọng nói
def hamnghe():
    nghe = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Translator: Tớ đang nghe nè")
        nghe.adjust_for_ambient_noise(mic)
        audio = nghe.record(mic, duration=4)  # chỉnh thời gian nếu You muốn nói lâu hoặc cho nó chạy nhanh hơn
        you = ""
    # audio = may_nghe.record(mic)
    # may_nghe.energy_thr(mic)
    # print("Translator:tớ đang suy nghĩ nha ...")
    try:
        you = nghe.recognize_google(audio, language="vi-VI")
        print("You: " + you)
    except Exception as e:
        print("Translator: Tớ ko hiểu" + str(e))
    return you
def noidungnoi():
    Input_text.delete("1.0", END)
    Input_text.insert("1.0", hamnghe())
    return

# hàm gửi tới mesTranslatorger
def gui():
    dichthuat()
    xoa()
    # băt buộc phải mở https://www.facebook.com/messages/t
    # pyautogui.click(112, 17)
    # vị trí tọa độ trên màn hình chỗ nhắn tin trên mess
    pyautogui.click(620, 740)
    # tự động dán nội dung đã copy
    pyautogui.hotkey('ctrl', 'v')
    # tự động nhấn enter để gửi
    pyautogui.press('enter')
    return


def dan():
    # tự động dán đã copy
    pyautogui.hotkey('ctrl', 'v')
    return

# nút Dịch
trans_btn = Button(root, text='Dịch VI-EN !', font='arial 12 bold', pady=0, command=dichthuat, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=380, y=40)
# nút xóa hết
trans_btn1 = Button(root, text='Xóa hết', font='arial 12 bold', pady=0, command=xoa, bg='royal blue1',
                    activebackground='sky blue')
trans_btn1.place(x=380, y=80)
# nút Giọng nói
trans_btn2 = Button(root, text='Giọng nói', font='arial 12 bold', pady=0, command=noidungnoi, bg='royal blue1',
                    activebackground='sky blue')
trans_btn2.place(x=380, y=120)
# nút gửi mess
trans_btn3 = Button(root, text='Gửi Messenger', font='arial 12 bold', pady=0, command=gui, bg='royal blue1',
                    activebackground='sky blue')
trans_btn3.place(x=380, y=160)
# nút dán
trans_btn4 = Button(root, text='Dán (past)', font='arial 12 bold', pady=0, command=dan, bg='royal blue1',
                    activebackground='sky blue')
trans_btn4.place(x=380, y=200)

# hàm bắt buộc để chạy giao diện 
root.mainloop()