ans = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())
if guess < ans:
    print("Please guess higher")
elif guess > ans:
    print("Please guess lower")
else:
    print("You got it first time")