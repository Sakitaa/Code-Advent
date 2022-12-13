with open('Day_7/input.txt') as f:
    data = f.read().splitlines()

allDirectories = {'/' : 0}

for line in data:
    caseDefiner = (lambda line: line.split(' '))(line)
    match caseDefiner[0]:
        case '$':
            if caseDefiner[1] == 'cd':
                currentDirectory = caseDefiner[2]
        case 'dir':
            allDirectories[caseDefiner[1]] = 0
        case other:
            allDirectories[currentDirectory] += int(caseDefiner[0])

for line in data:
    caseDefiner = (lambda line: line.split(' '))(line)
    match caseDefiner[0]:
        case '$':
            if caseDefiner[1] == 'cd':
                currentDirectory = caseDefiner[2]
        case 'dir':
            allDirectories[currentDirectory] += allDirectories[caseDefiner[1]]

totalSum = 0
for key in allDirectories.keys():
    value = allDirectories[key]
    if value <= 100000:
        totalSum += value

print('sum', totalSum)
