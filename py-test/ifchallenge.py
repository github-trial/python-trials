name = input("What is your name? ")
age  = int(input("How old are you? "))

if 18 <= age < 31:
    print("{} you are eligible to go on vacation".format(name))
else:
    print("{} your are not eligible to go on vacation".format(name))
