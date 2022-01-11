name = "stefyvarghese"

letter = input("Enter a Char: ")

if letter in name:
    print("{} is in  {}".format(letter, name))
else:
    print("{} is not in {}".format(letter, name))