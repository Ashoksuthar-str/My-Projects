import random
import time
import string

#You can also use coll list for letters.

#coll = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spc = string.printable

#Write anything Here in HW Variable
HW = ("Hello World !!")
final = []
n = [""]
for i in range(0,len(HW)):
	while n[0] != HW[i]:
		n[0] = random.choice(spc)
		print(*final,*n,sep="")
		time.sleep(0.03)
	final.append(*n)
for i in range(5):
	print(*final,sep="")
	time.sleep(0.5)