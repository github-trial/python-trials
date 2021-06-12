for i in range(1, 13):
    print("No. {} sqared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("-" * 40)

name = input("Please Enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 20:
    print("you are old enough to get vaccinated")
else:
    print("you have to wiat till slots are open")

if age < 20:
    print("Please come back in {0} years".format(20 -age))
elif age == 100:
    print("You are over age")
else:
    print("You are old")