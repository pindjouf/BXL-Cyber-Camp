import random

secret_number = random.randint(1, 100)
answer_found = False

print("Welcome to the Number Guessing Game!")

while not answer_found:
	guess = input("Guess a number between 1 and 100: ")
	while guess[0] == '-':
		print("You shouldn't put a negative number!")
		guess = input("Try again: ")
	# This condition checks if its a digit or not
	if guess.isdigit():
		guess = int(guess)
		# This condition checks if its between 0 and 100
		if guess > 0 and guess <= 100:
			if guess == secret_number:
				print("you found it!")
				found = True
			elif guess < secret_number:
				print("It's higher")
			elif guess > secret_number:
				print("It's lower")
		else:
			print("value has to be between 1 and 100")
	else:
		print("yo, put a number man!")
print("end")
