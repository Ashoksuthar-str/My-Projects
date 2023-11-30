while True:
	n = int(input(':'))
	c = 0
	if n == 0:
		break
	else:
		for i in range(1,n):
			if n%i==0:
				c += 1		
	if c==1:
		print('its prime')