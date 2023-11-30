def main():
	n = input('HOW MANY YOU WANT MAKE A TRIANGLE(0 or 1 = quit): ')
	if int(n)== 0 or int(n) == 1:
		print(' byy!!')
	else:
		for i in range(1,int(n)+1):
			for y in range(int(n)-i):
				print("*",end='')
			print()
		main()
		
main()