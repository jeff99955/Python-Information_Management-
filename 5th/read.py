gradestr = input()
grades = gradestr.split()
intgrades = []

for i in grades:
    intgrades.append(int(i))

print(intgrades)