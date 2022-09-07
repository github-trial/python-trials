#Take input from the user
from posixpath import split
from sre_parse import parse_template
from unittest import result


user_input = input("Please enter three numbers: ")

#split the given input string into 3 parse_template
string_split = user_input.split(",")
print(user_input)

int_split = []
for ss in string_split:
    int_split.append(int(ss))
    print(int_split)

# calculate result a + b - c
a, b, c = int_split

result = a + b - c
print(result)

