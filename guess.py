import random


def random_number(start,end):
	'''
	Python project to guess a number that has randomly been selected
	'''
	return random.randrange(start,end)

def perfect_guess(guess, generated_number):
	if guess < generated_number:
		return "This is lower. Please try again."
	elif guess > generated_number:
		return "This is higher. Please try again."
	else:
		return "This is the correct number, Bye!"
	


number = random_number(0,5)
while True:
	response=input("Please input a number between 0 and 5:")
	try:
		value = int(response)
		res = perfect_guess(value, number)
		if(res == "This is the correct number, Bye!"):
			print(res)
			break
		print(res)
	except ValueError:
		print("This is not a valid integer. Please try again")
		continue

	
