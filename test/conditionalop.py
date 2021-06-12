answer = 5
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, the guess is incorrect")
elif guess > answer:
    print("Pleas guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, the guess is incorrect")
else:
    print("You got it first time")