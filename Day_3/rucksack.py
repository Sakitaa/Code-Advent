with open('Day_3/input.txt') as f:
    data = f.read().splitlines()

priorities = 0

for line in data:
    word = ""
    temp = priorities
    for j in range(int(len(line)/2), len(line)):
        word += line[j]
    for x in range(0, int(len(line)/2)+1):
        result = word.find(line[x])
        if result >=0 and temp == priorities:
            if ord(line[x]) > 96:
                priorities += ord(line[x])-96
            else:
                priorities += ord(line[x])-38

print("Part One")
print("Total sum of priorities: ", priorities)


i = 0
word1 = ""
word2 = ""
word3 = ""
badgeValues = 0

for line in data:
    temp = badgeValues
    if i == 0:
        word1 = str(line)
        i += 1
    elif i == 1:
        word2 = str(line)
        i += 1
    elif i == 2:
        word3 = str(line)
        i = 0
        for x in range(0, int(len(word1))):
            for y in range(0, int(len(word2))):
                if word1[x] == word2[y]:
                    for z in range(0, int(len(word3))):
                        if word3[z] == word2[y] and temp == badgeValues:
                            if ord(word3[z]) > 96:
                                badgeValues += ord(word3[z])-96
                                break
                            else:
                                badgeValues += ord(word3[z])-38
                                break

print("Part Two")
print("Total sum of badge values:", badgeValues)
