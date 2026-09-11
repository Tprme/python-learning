while True:
	password = input("清输入你的密码(输入exit退出):")


	if password == "exit":
 	    print("退出程序")
 	    break


	length = len(password)
	has_digit = False
	has_alpha = False


	for char in password:
	    if char.isdigit():
	        has_dight = True
	    elif char.isalpha():
	        has_alpha = True


	if length >= 8 and has_dight and has_alpha:
	    print("密码强度：强")
	else:
	    print("密码强度：弱，建议更改！")

