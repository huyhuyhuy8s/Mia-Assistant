def language():
	print("------------------------------------------")
	file1 = open("language.txt","w") 
	L = input("VI for Vietnamese or EN for English.\nVI cho Tiếng Việt hoặc EN cho Tiếng Anh. \nSelect language (Chọn ngôn ngữ): ")
	file1.write(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("language.txt","r+")  
	language=file1.read()
	print("Output of Read function is (Kết quả ghi được): "+ language)

def theme():	
	print("------------------------------------------")
	file1 = open("theme.txt","w") 
	L= input("Choose your theme <Dark or Light>: \n Chọn giao diện <Tối(D) hoặc Sáng(L)>")
	file1.write(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("theme.txt","r+")  
	theme=file1.read()
	print ("Output of Read function is (Kết quả ghi được): " + theme)

def username():
	print("------------------------------------------")
	file1 = open("username.txt","w") 
	L= input("Enter User_name (Nhập tên người dùng): ")
	file1.write(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("username.txt","r+")  
	username=file1.read()
	print ("Output of Read function is (Kết quả ghi được): " + username)

def main():
	language()
	username()
	theme()
	
if __name__ == "__main__":
	main()