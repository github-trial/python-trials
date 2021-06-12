numbers = "4,358;829,278:2689;78"
seperators = ""

for char in numbers:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators) 

values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int(val) for val in values])