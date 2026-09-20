numberlist = [1, 2, 3, 5, 7, 6, 9, 11, 12, 18, 19, 21]

first_even = None
for i in range(len(numberlist)):
    if numberlist[i] % 2 == 0:
        if first_even is None:
            first_even = i
        last = i

if first_even is not None and first_even != last:
    numberlist[first_even], numberlist[last] = numberlist[last], numberlist[first_even]
print(numberlist)
        