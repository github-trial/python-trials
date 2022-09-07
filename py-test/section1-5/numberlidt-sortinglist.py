even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(even)
print(odd)

odd.extend(even)
even.sort(reverse=True)

print(even)