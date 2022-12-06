with open('Day_6/input.txt') as f:
    data = f.read()

# First attempt, works but a lot of manual changes for different inputs
#for i in range(3, int(len(data))-1):
#    if data[i-3] != data[i-2] and data[i-3] != data[i-1] and data[i-3] != data[i]:
#        if data[i-2] != data[i-1] and data[i-2] != data[i]:
#            if data[i-1] != data[i]:
#                i += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
#                break

# Second attemp much better in terms of changing for part two
forCheck = 0
partOne = 4 # number of char to check in string for part one x = 4
for i in range(1, partOne):
    forCheck += i

for j in range(3, int(len(data))):
    text = ""
    check = 0
    for k in range(4, 0, -1):
        text += data[j-k+1]
    for l in range(0, int(len(text))-1):
        for g in range(l+1, int(len(text))):
            if text[l] != text[g]:
                check += 1
    if check == forCheck:
        j += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
        break

print("Part One")
print("Number of characters processed:", j)

forCheck = 0
partTwo = 14 # number of char to check in string for part two x = 14
for i in range(1, partTwo):
    forCheck += i

for x in range(13, int(len(data))):
    text = ""
    check = 0
    for k in range(14, 0, -1):
        text += data[x-k+1]
    for l in range(0, int(len(text))-1):
        for g in range(l+1, int(len(text))):
            if text[l] != text[g]:
                check += 1
    if check == forCheck: 
        x += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
        break

print("Part Two")
print("Number of characters processed:", x)

