with open('Day_7/input.txt') as f:
    data = f.read().splitlines()

import operator

def rindex(lst, value):
    return len(lst) - operator.indexOf(reversed(lst), value) - 1


dataDict = {}
dataAdd = {}
dataList = []
totalSum = 0
for line in data:
    caseDefiner = (lambda line: line.split(' '))(line)
    match caseDefiner[0]:
        case '$':
            if caseDefiner[1] == 'cd' and caseDefiner[2] != '..':
                currentDir = caseDefiner[2]
                dataList.append(currentDir)
                dataDict[rindex(dataList, currentDir)] = 0
        case 'dir':
            dataAdd[caseDefiner[1]] = dataList.index(currentDir)
        case other:
            totalSum += int(caseDefiner[0])
            check = rindex(dataList, currentDir)
            dataDict[rindex(dataList, currentDir)] += int(caseDefiner[0])

for key, value in reversed(dataAdd.items()):
    dataDict[value] += dataDict[rindex(dataList, key)]

sum = 0
for key, value in dataDict.items():
    if value < 100_000:
        print(key, value)
        sum += value


print(sum)

testDict = {
    '/': {
        'a': {
            'e': {
                'i': 584
            },
            'f': 29_116,
            'g': 2_557,
            'h.lst': 62_596
        },
        'b.txt': 14_848_514,
        'c.dat': 8_504_156,
        'd': {
            'j': 4_060_174,
            'd.log': 8_033_020,
            'd.ext': 5_626_152,
            'k': 7_214_296,
        }
    }
}
    #  e is 584 
    #  a ia 94,853 
    #  d is 24,933,642
    # / is 48,381,165