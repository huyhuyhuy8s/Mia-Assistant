def language(L):
	print("------------------------------------------")
	if L == "Vietnamese" or L == "Tiếng Việt":
		L = "VI"
		file1 = open("language.txt","w") 
		file1.write(L)
		file1.close()
	elif L == "English" or L == "Tiếng Anh":
		L = "EN"
		file1 = open("language.txt","w") 
		file1.write(L)
		file1.close() 
	else:
		pass
	# L = input("VI for Vietnamese or EN for English.\nVI cho Tiếng Việt hoặc EN cho Tiếng Anh. \nSelect language (Chọn ngôn ngữ): ")
	
	 #to change file access modes 
	return L
	file1 = open("language.txt","r+")  
	language=file1.read()
	print("Output of Read function is (Kết quả ghi được): "+ language)

def theme(L):	
	print("------------------------------------------")
	if L == "Light" or L == "Sáng":
		L = "L"
		file1 = open("theme.txt","w") 
		file1.write(L)
		file1.close()
	elif L == "Dark" or L == "Tối":
		L = "D"
		file1 = open("theme.txt","w") 
		file1.write(L)
		file1.close() 
	else:
		pass
	  
	# L= input("Choose your theme <Dark or Light>: \n Chọn giao diện <Tối(D) hoặc Sáng(L)>")
	return L
	file1 = open("theme.txt","r+")  
	theme=file1.read()
	print ("Output of Read function is (Kết quả ghi được): " + theme)

def username(L):
	print("------------------------------------------")
	if L == "":
		return L
	else:
		file1 = open("username.txt","w") 
		file1.write(L) 
		file1.close() #to change file access modes 
		return L
	# L= input("Enter User_name (Nhập tên người dùng): ")
	file1 = open("username.txt","r+")  
	username=file1.read()
	print ("Output of Read function is (Kết quả ghi được): " + username)
	
# def main():
# 	language()
# 	username()
# 	theme()
	
# if __name__ == "__main__":
# 	main()