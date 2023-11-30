import random

number = random.randint(1,50)
count = 0

print("Guess a number between 1 to 50 \n You have 10 Tries")

while True:
	ans = int(input("enter your number : "))
	if ans > number:
		print("to high")

		count += 1
	
	if ans < number:
		print("to low")
		count += 1
	
	if count == 10:
		print("Your tries are over")
		break
		
	if ans == number:
		print("you are right")
		break