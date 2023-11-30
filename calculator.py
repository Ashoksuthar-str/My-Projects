def calculater():
	type = input(" Enter what you want to do. \n If you want to add type (1) \n If you want to subtract type (2) \n If you want to multyply type (3) \n If you want to devid type (4) \n (Type (0) if you want to fuck-off) \n :")
	if int(type)== 1:
		a = input('Enter your first digit: ')
		b = input('Enter your second digit: ')
		n = int(a) + int(b)
		print("Your answer is:",n)
		yn=input("Wants to calculate again (y/n): ")
		if str(yn) == "y":
			calculater()
		else:
			print("byy")
	elif int(type)== 2:
		a = input('Enter your first digit: ')
		b = input('Enter your second digit: ')
		n = int(a) - int(b)
		print("Your answer is:",n)
		yn=input("Wants to calculate again (y/n): ")
		if str(yn) == "y":
			calculater()
		else:
			print("byy")
	elif int(type)== 3:
		a = input('Enter your first digit: ')
		b = input('Enter your second digit: ')
		n = int(a) * int(b)
		print("Your answer is:",n)
		yn=input("Wants to calculate again (y/n): ")
		if str(yn) == "y":
			calculater()
		else:
			print("byy")
	if int(type)== 4:
		a = input('Enter your first digit: ')
		b = input('Enter your second digit: ')
		n = int(a) / int(b)
		print("Your answer is:",n)
		yn=input("Wants to calculate again (y/n): ")
		if str(yn) == "y":
			calculater()
		else:
			print("byy")
	if int(type) == 0:
		print(" Fuck-off.")
	else:
		print('Please choose a valid number: ')
		calculater()
calculater()