a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []

for i in a:
    if i not in b and i not in c:
        c.append(i)

for i in b:
    if i not in a and i not in c:
        c.append(i)
        
print(c)