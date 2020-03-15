intl = [] #declare an empty list
print(intl)
intl = [0] * 10
print(intl)
for i in intl:
    print(type(i), i)
intl.append("XD")
for i in intl:
    print(type(i), i)
#note that there can be various type in a list
intl.append([8,7,6,5])
print(intl[len(intl) - 1][0])
intl = [3, 4, 1, 2, 7, 8]
print(intl)
intl.insert(2, 4)
print(intl)
print(intl.count(4))
print(intl.index(4))
intl.sort()
print(intl)
intl.reverse()
print(intl)
intl.pop(4)
print(intl)