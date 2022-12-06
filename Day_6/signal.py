with open('Day_6/input.txt') as f:
    data = f.read()

for i in range(3, int(len(data))-1):
    if data[i-3] != data[i-2] and data[i-3] != data[i-1] and data[i-3] != data[i]:
        if data[i-2] != data[i-1] and data[i-2] != data[i]:
            if data[i-1] != data[i]:
                i += 1 # because first index is 0 and not 1 we have to add 1 to get the correct result
                break

print("Number of characters processed:", i)