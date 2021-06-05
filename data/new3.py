def language(L):
	if L == "Vietnamese" or L == "Tiếng Việt":
		file1 = open("language.txt","w") 
		file1.write("VI")
		file1.close()
	elif L == "English" or L == "Tiếng Anh":
		file1 = open("language.txt","w") 
		file1.write("EN")
		file1.close() 
	else:
		pass

def theme(L):	
	if L == "Light" or L == "Sáng":
		file1 = open("theme.txt","w") 
		file1.write("L")
		file1.close()
	elif L == "Dark" or L == "Tối":
		file1 = open("theme.txt","w") 
		file1.write("D")
		file1.close() 
	else:
		pass

def username(L):
	if L == "":
		return "Admin"
	else:
		file1 = open("username.txt","w") 
		file1.write(L) 
		file1.close() 