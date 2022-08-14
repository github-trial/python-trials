pangram = "This is Sorting testing"
letters = sorted(pangram)
print(letters)

numbers = [1.1, 2.4, 4.3, 8.6,9.4, 3.2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("This is Sorting testing",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "stefy",
         "Tom"]
names.sort(key=str.casefold)
print(names)
