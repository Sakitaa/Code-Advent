with open('Day_6/input.txt') as f:
    data = f.read()

for i in range(3, int(len(data))-1):
    if data[i-3] != data[i-2] and data[i-3] != data[i-1] and data[i-3] != data[i]:
        if data[i-2] != data[i-1] and data[i-2] != data[i]:
            if data[i-1] != data[i]:
                i += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
                break

for j in range(3, int(len(data))):
    text = ""
    check = 0
    for k in range(4, 0, -1):
        text += data[j-k+1]
    for l in range(0, int(len(text))-1):
        for g in range(l+1, int(len(text))):
            if text[l] != text[g]:
                check += 1
    if check == 6:
        j += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
        break

print("Part One")
print("Number of characters processed:", i)
print("Number of characters processed:", j)