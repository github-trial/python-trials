print("Please choose the option from the list below:")
print("1:\t Learn Python")
print("2:\t Learn Java")
print("3:\t Learn ASP")
print("4:\t Learn Tf")
print("5:\t Learn HTML")
print("0:\t Exit")

while True:
    choice = input()
    if choice == 0:
        break
    elif choice in "12345":
        print("You chose {}".format(choice))

