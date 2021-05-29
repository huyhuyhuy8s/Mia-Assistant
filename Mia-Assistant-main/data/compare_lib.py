def VN_compare(you,username,loichao,volume,temp):
	if "Chào" in you or "Xin chào" in you or "Hello" in you:
		mia_brain = mia.VN_hi(loichao)
		return mia_brain
	elif "dịch" in you or "từ điển" in you:
		mia_brain = mia.VN_trans()
		return mia_brain
	elif "Flappy Bird" in you:
		mia_brain = mia.VN_Flappybird()
		return mia_brain
	elif "yêu" in you or "love" in you or "Yêu" in you:
		mia_brain = mia.VN_love()
		return mia_brain
	elif "ngày" in you:
		mia_brain = mia.VN_day()
		return mia_brain
	elif "giờ" in you:
		mia_brain = mia.VN_clock()
		return mia_brain
	elif "Play" in you or "play" in you or "nhạc" in you or "Bật nhạc" in you or "bật nhạc" in you or "Music" in you or "music" in you or "Youtube" in you or "youtube" in you:
		if "Play music" == you or "play music" == you or "Bật nhạc" == you or "bật nhạc" == you or  "Âm nhạc" == you or "âm nhạc" == you or "music" == you or "Music" == you or "Youtube" == you or "youtube" == you:
			mia_brain = "Đang mở youtube"
			webbrowser.open('https://www.youtube.com/',new=1)
			print(mia_brain)
			mia.noi(gTTS(mia_brain,lang='vi',slow=False))
			runai=2
			return runai
		else:
			mia_brain = mia.VN_music(you)
			return mia_brain
	elif "Opera" in you or "Google" in you or "duyệt web" in you or "Duyệt web" in you or "Lướt web" in you: 
		mia_brain = mia.VN_browser()
		return mia_brain
	elif "tìm kiếm" in you or "Tìm kiếm" in you:
		mia_brain = mia.VN_search()
		return mia_brain
	elif "Facebook" in you:
		mia_brain = mia.VN_facebook()
		return mia_brain
	elif "Wikipedia" in you or "wiki" in you or "Wiki" in you or "Bách khoa toàn thư" in you:
		mia_brain = mia.VN_wikipedia()
		return mia_brain
	elif "tắt máy" in you or "Tắt máy" in you or "Shut down" in you or "shut down" in you:
		mia_brain = mia.VN_shutdown()
		return mia_brain
	elif "khởi động lại" in you or "Khởi động lại" in you or "restart" in you or "Restart" in you:
		mia_brain = mia.VN_restart()
		return mia_brain
	elif "nghỉ ngơi" in you or "Nghỉ ngơi" in you or "break" in you:
		mia_brain = mia.VN_break()
		return mia_brain
	elif "Ngủ" in you or "ngủ" in you or "sleep" in you or "Sleep" in you:
		mia_brain = mia.VN_sleep()
		return mia_brain
	elif "bye" in you or "tạm biệt" in you or "Tạm biệt" in you:
		mia_brain = mia.VN_bye()
		return mia_brain
	elif "Good night" in you or "goodnight" in you:
		mia_brain = mia.VN_goodnight()
		return mia_brain
	elif "what the f***" in you or "What the f***" in you:
		mia_brain = "fuck you"
		return mia_brain
	elif "giảm volume" in you or "giảm âm lượng" in you:
		mia_brain = mia.VN_volumedown(volume)
		return mia_brain
	elif "tăng volume" in you or "tăng âm lượng" in you:
		mia_brain = mia.VN_volumeup(volume)
		return mia_brain
	elif "đọc báo" in you or "Đọc báo" in you:
		if "Đọc báo" == you or "đọc báo" == you:
			mia_brain = "Đang mở Vnexpress"
			webbrowser.open('https://vnexpress.net',new=1)
			print(mia_brain)
			mia.noi(gTTS(mia_brain,lang='vi',slow=False))
			runai=2
			return runai
		# elif "Đọc báo " in you or "đọc báo " in you:
		# 	x = you[you.index("báo ")+4:]
		# 	mia_brain = mia.VN_newspaper(you,x)
		# 	# os.system("pause")
		# 	return mia_brain
		elif "Đọc báo về " in you or "đọc báo về " in you:
			x = you[you.index("về ")+3:]
			mia_brain = mia.VN_newspaper(you,x)
			# os.system("pause")
			return mia_brain
	elif "cài đặt" in you or "tùy chỉnh" in you or "setting" in you or "option" in you or "config" in you:
		mia_brain = mia.VN_setting()
		return mia_brain
	elif "dạy" in you:
		mia_brain = mia.VN_teach()
		return mia_brain
	elif "Ok" in you or "ok" in you or "OK" in you:
		webbrowser.open_new(temp)
		mia_brain="Đang mở "
		print(mia_brain + temp)
		mia.noi(gTTS(mia_brain,lang='vi',slow=False))
		time.sleep(5)
		# os.system("pause")
		runai=1
		return runai
	elif "stop" in you or "exit" in you or "thoát" in you:
		mia_brain = mia.VN_exit()
		return mia_brain


def EN_compare(you,username,loichao,volume,temp):
	if "Hi" in you or "Hello" in you or "hi" in you or "hello" in you:
		mia_brain = mia.EN_hi(loichao)
		return mia_brain
	elif "translate" in you or "Translate" in you:
		mia_brain = mia.EN_trans()
		return mia_brain
	elif "Flappy Bird" in you:
		mia_brain = mia.EN_Flappybird()
		return mia_brain
	elif "love" in you:
		mia_brain = mia.EN_love()
		return mia_brain
	elif "today" in you or "date" in you or "day" in you:
		mia_brain = mia.EN_day()
		return mia_brain
	elif "time" in you:
		mia_brain = mia.EN_clock()
		return mia_brain
	elif "Play" in you or "play" in you or "Music" in you or "music" in you or "Youtube" in you or "youtube" in you:
		if "Play music" == you or "play music" == you or "music" == you or "Music" == you or "Youtube" == you or "youtube" == you:	
			mia_brain = "Opening Youtube"
			webbrowser.open('https://www.youtube.com/',new=1)
			print(mia_brain)
			say(mia_brain)
			runai=2
			return runai
		else:
			mia_brain = mia.EN_music(you)
			return mia_brain
	elif "Opera" in you or "Google" in you or "webbrowser" in you or "Webbrowser" in you: 
		mia_brain = mia.EN_browser()
		return mia_brain
	elif "search" in you:
		mia_brain = mia.EN_search()
		return mia_brain
	elif "Facebook" in you:
		mia_brain = mia.EN_facebook()
		return mia_brain
	elif "Wikipedia" in you:
		mia_brain = mia.EN_wikipedia()
		return mia_brain
	elif "Turn off" in you or "turn off" in you or "Shut down" in you or "shut down" in you:
		mia_brain = mia.EN_shutdown()
		return mia_brain
	elif "restart" in you or "Restart" in you:
		mia_brain = mia.EN_restart()
		return mia_brain
	elif "Break" in you or "break" in you:
		mia_brain = mia.EN_break()
		return mia_brain
	elif "sleep" in you or "Sleep" in you:
		mia_brain = mia.EN_sleep()
		return mia_brain
	elif "bye" in you or "Bye" in you:
		mia_brain = mia.EN_bye()
		return mia_brain
	elif "Goodnight" in you or "goodnight" in you:
		mia_brain = mia.EN_goodnight()
		return mia_brain
	elif "what the f***" in you:
		mia_brain = "fuck you"
		return mia_brain
	elif "volume down" in you:
		mia_brain = mia.EN_volumedown(volume)
		return mia_brain
	elif "volume up" in you:
		mia_brain = mia.EN_volumeup(volume)
		return mia_brain
	elif "newspaper" in you or "reading newspaper" in you or "read newspaper" in you:
		if "reading newspaper" == you or "read newspaper" == you or "newspaper" == you:
			mia_brain = "Opening Vnexpress"
			webbrowser.open('https://www.nytimes.com',new=1)
			print(mia_brain)
			say(mia_brain)
			runai=2
			return runai
		# elif "read newspaper " in you or "reading newspaper " in you or "newspaper " in you:
		# 	x = you[you.index("newspaper ")+10:]
		# 	mia_brain = EN_newspaper(you,x)
		# 	# os.system("pause")
		# 	return mia_brain
		elif "read newspaper about" in you or "reading newspaper about" in you or "newspaper about" in you:
			x = you[you.index("about ")+6:]
			mia_brain = mia.EN_newspaper(you,x)
			# os.system("pause")
			return mia_brain
	elif "config" in you or "configure" in you or "setting" in you or "option" in you:
		mia_brain = mia.EN_setting()
		return mia_brain
	elif "teach" in you or "teaching" in you or "study" in you:
		mia_brain = mia.EN_teach()
		return mia_brain
	elif "Ok" in you or "ok" in you or "OK" in you:
		webbrowser.open_new(temp)
		mia_brain="Opening "
		print(mia_brain + temp)
		say(mia_brain)
		time.sleep(5)
		runai=1
		return runai
	elif "stop" in you or "exit" in you:
		mia_brain = mia.EN_exit()
		return mia_brain

def users_compare(you,username,loichao,volume):
	if "username" in you:
		mia_brain = username
		return mia_brain
	elif "x`" in you:
		mia_brain = " "
		return mia_brain
	elif "Phạm Đình Đoàn" in you:
		mia_brain = "hello hữu sơn"
		return mia_brain
	elif "cuộc thi khoa học kĩ thuật" in you:
		mia_brain = "rất thú vị"
		return mia_brain
	elif "cuộc thi khoa học kỹ thuật" in you:
		mia_brain = "Rất thú vị"
		return mia_brain
	elif "không nói nữa" in you:
		mia_brain = "Không"
		return mia_brain