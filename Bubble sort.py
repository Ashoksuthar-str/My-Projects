n = []
element = int(input('Enter the number of element in array : '))
for i in range(element):
	n.append(int(input('Enter Number : ')))
print("\n\nList : ",n)
a = 0
b = 0
c = 0
for r in range(14):#Value 14 is a constant which can be changed if the number of element is high

	for i in range(len(n)-1):
		a = n[i]
		b = n[i+1]
		if n[i] > n[i+1]:
			c = a
			n[i] = b
			n[i+1] = c
print("Low to HIGH :",n)
for r in range(14):#Value 14 is a constant which can be changed if the number of element is high

	for i in range(len(n)-1):
		a = n[i]
		b = n[i+1]
		if n[i] < n[i+1]:
			c = a
			n[i] = b
			n[i+1] = c
print("High to Low",n)