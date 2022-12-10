with open('Day_7/input.txt') as f:
    data = f.read().splitlines()

fileSizeSum = 0

def ifCommand(line):
    print('Command type', line)

def ifDirectory(line):
    global fileSizeSum
    print('Directory name', line)
    fileSizeSum = 0
    print('File size sum', fileSizeSum)

def ifOther(line):
    global fileSizeSum
    print('File size', line)
    fileSizeSum += int(line)
    print('File size sum', fileSizeSum)

for line in data:
    caseDefiner = (lambda line: line.split(' '))(line)
    match caseDefiner[0]:
        case '$': ifCommand(caseDefiner[1])
        case 'dir': ifDirectory(caseDefiner[1])
        case other: ifOther(caseDefiner[0])