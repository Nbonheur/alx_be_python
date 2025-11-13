answer = 5

print("Guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
	print("Guess higher")

	guess = int(input())
	if answer > guess:
		print("Guess lower")

	elif guess < answer:
		print("Try one more time")

	else:
		print("Now you got it!")

elif guess > answer:
	print("Guess lower")

	guess = int(input())
	if answer < answer:
                print("Guess higher")

        	elif guess > answer:
                	print("Try again!")

        	else:
                	print("Congz you got it!")

else:
	print("You got it first time")
	print("Well done!")
