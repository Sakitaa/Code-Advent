with open('Day_7/input.txt') as f:
    data = f.read().splitlines()

fileSizeSum = 0
directorySizes = []
directoryIndex = 0

def ifCommand(commandType):
    print('Command type', commandType)

def ifDirectory(directoryName):
    global fileSizeSum
    fileSizeSum = 0
    if len(directorySizes) == 0:
        global directoryIndex
        directoryIndex = 0
    else:
        directoryIndex += 1

def ifOther(fileSize):
    global fileSizeSum
    fileSizeSum += int(fileSize)
    global directoryIndex
    global directorySizes
    directorySizes.insert(directoryIndex, fileSizeSum)

for line in data:
    caseDefiner = (lambda line: line.split(' '))(line)
    match caseDefiner[0]:
        case '$':
            match caseDefiner[1]:
                case 'cd':
                    if caseDefiner[1] == 'cd':
                        print('cd', caseDefiner[2])
                case 'ls':
                    ifCommand(caseDefiner[1])
        case 'dir': ifDirectory(caseDefiner[1])
        case other: ifOther(caseDefiner[0])

temp = 0
for i in range(0, int(len(directorySizes))):
    if directorySizes[i] < 100_000:
        print(temp)
        temp += directorySizes[i]
print(temp)