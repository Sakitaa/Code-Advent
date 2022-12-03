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

print("Total sum of priorities: ", priorities)