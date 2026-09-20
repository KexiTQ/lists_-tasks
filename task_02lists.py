numberlist = [1, 2, 3, 5, 7, 6, 9, 11, 12, 18, 19, 21]

min_number = numberlist[0]
max_number = numberlist[0]

for i in numberlist:
    if i < min_number:
            min_number = i
    if i > max_number:
        max_number = i

print(min_number + max_number)
