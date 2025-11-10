age = int(input("Enter your age: "))


if age >= 100:
	print("You time for voting is done please leave it to younger generation")
elif age >= 18:
	print("You are eligible to vote.")
else:
	print(f"You are not eligible to vote, come in {18-age} years")
