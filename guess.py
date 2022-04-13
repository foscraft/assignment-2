import random
'''
Python project to guess a number that has randomly been selected
'''

def random_number(start,end):
	return random.randrange(start,end)

def perfect_guess():
	number = random_number(0,5)
	guess="wrong"
	while guess=="wrong":
		response=input("Please input a number between 0 and 5:")
		try:
			value = int(response)
		except ValueError:
			print("This is not a valid integer. Please try again")
			continue
		value = int(response)
		if value < number:
			print("This is lower. Please try again.")
		elif value > number:
			print("This is higher. Please try again.")
		else:
			print("This is the correct number, Bye!")
			guess="correct"

random_number(0,5)
perfect_guess()
