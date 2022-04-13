import random
'''
Python project to guess a number that has randomly been selected
'''
def perfectGuess():

	number=random.randrange(0,5)
	guess="wrong"
	print("Welcome to Skaehub Guess Game")

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

perfectGuess()
