with open('Day_4/input.txt') as f:
    data = f.read().splitlines()

fullOverlap = 0
for line in data:
    temp = fullOverlap
    check = line.split()
    x = [item.split(',') for item in check]
    x = [item for l in x for item in l]
    x = [item.split("-") for item in x]
    x = [item for l in x for item in l]
    if int(x[0]) <= int(x[2]) and int(x[1]) >= int(x[3]):
            fullOverlap += 1
    elif int(x[2]) <= int(x[0]) and int(x[3]) >= int(x[1]):
            fullOverlap += 1

print("Part One")
print("Number of full overlaps:", fullOverlap)

anyOverlap = 0
for line in data:
    temp = anyOverlap
    check = line.split()
    x = [item.split(',') for item in check]
    x = [item for l in x for item in l]
    x = [item.split("-") for item in x]
    x = [item for l in x for item in l]
    if (int(x[0]) <= int(x[2]) <= int(x[1])) or (int(x[0]) <= int(x[3]) <= int(x[1])):
            anyOverlap += 1
    elif (int(x[2]) <= int(x[0]) <= int(x[3])) or (int(x[2]) <= int(x[1]) <= int(x[3])):
            anyOverlap += 1

print("Part Two")
print("Number of any overlaps:", anyOverlap)