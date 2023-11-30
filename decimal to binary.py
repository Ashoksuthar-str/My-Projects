a =[]
n = int(input(':'))
while n>=1:
	if int(n)%2 == 0:
		a.append(0)
	else:
		a.append(1)
	n = n/2

if n == 0:
	a.append(1)
l = len(a)
for i in range(l):
	print(a[l-i-1],end='')