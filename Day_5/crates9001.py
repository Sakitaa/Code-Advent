with open('Day_5/input.txt') as f:
    data = f.read().splitlines()

stack1 = []
stack1.append('P')
stack1.append('F')
stack1.append('M')
stack1.append('Q')
stack1.append('W')
stack1.append('G')
stack1.append('R')
stack1.append('T')

stack2 = []
stack2.append('H')
stack2.append('F')
stack2.append('R')

stack3 = []
stack3.append('P')
stack3.append('Z')
stack3.append('R')
stack3.append('V')
stack3.append('G')
stack3.append('H')
stack3.append('S')
stack3.append('D')

stack4 = []
stack4.append('Q')
stack4.append('H')
stack4.append('P')
stack4.append('B')
stack4.append('F')
stack4.append('W')
stack4.append('G')

stack5 = []
stack5.append('P')
stack5.append('S')
stack5.append('M')
stack5.append('J')
stack5.append('H')

stack6 = []
stack6.append('M')
stack6.append('Z')
stack6.append('T')
stack6.append('H')
stack6.append('S')
stack6.append('R')
stack6.append('P')
stack6.append('L')

stack7 = []
stack7.append('P')
stack7.append('T')
stack7.append('H')
stack7.append('N')
stack7.append('M')
stack7.append('L')

stack8 = []
stack8.append('F')
stack8.append('D')
stack8.append('Q')
stack8.append('R')

stack9 = []
stack9.append('D')
stack9.append('S')
stack9.append('C')
stack9.append('N')
stack9.append('L')
stack9.append('P')
stack9.append('H')

print("Top of each stack before:", stack1[len(stack1)-1] + 
stack2[len(stack2)-1] + stack3[len(stack3)-1] + 
stack4[len(stack4)-1] + stack5[len(stack5)-1] + 
stack6[len(stack6)-1] + stack7[len(stack7)-1] + 
stack8[len(stack8)-1] + stack9[len(stack9)-1])

for line in data:
    line = line.split()
    howMany = int(line[1])
    fromWhere = int(line[3])
    toWhere = int(line[5])

    match fromWhere:
        case 1: fromWhere = stack1
        case 2: fromWhere = stack2
        case 3: fromWhere = stack3
        case 4: fromWhere = stack4
        case 5: fromWhere = stack5
        case 6: fromWhere = stack6
        case 7: fromWhere = stack7
        case 8: fromWhere = stack8
        case 9: fromWhere = stack9
    
    match toWhere:
        case 1: toWhere = stack1
        case 2: toWhere = stack2
        case 3: toWhere = stack3
        case 4: toWhere = stack4
        case 5: toWhere = stack5
        case 6: toWhere = stack6
        case 7: toWhere = stack7
        case 8: toWhere = stack8
        case 9: toWhere = stack9

    length = int(len(fromWhere))
    for i in range(0, howMany):
        popped = fromWhere[length-howMany]
        toWhere.append(popped)
        fromWhere.pop(length-howMany)

    match int(line[3]):
        case 1: stack1 = fromWhere
        case 2: stack2 = fromWhere
        case 3: stack3 = fromWhere
        case 4: stack4 = fromWhere
        case 5: stack5 = fromWhere 
        case 6: stack6 = fromWhere 
        case 7: stack7 = fromWhere
        case 8: stack8 = fromWhere
        case 9: stack9 = fromWhere
    
    match int(line[5]):
        case 1: stack1 = toWhere
        case 2: stack2 = toWhere
        case 3: stack3 = toWhere
        case 4: stack4 = toWhere
        case 5: stack5 = toWhere 
        case 6: stack6 = toWhere 
        case 7: stack7 = toWhere
        case 8: stack8 = toWhere
        case 9: stack9 = toWhere
        

print("Top of each stack(FFRGHLLRH):", stack1[len(stack1)-1] + 
stack2[len(stack2)-1] + stack3[len(stack3)-1] + 
stack4[len(stack4)-1] + stack5[len(stack5)-1] + 
stack6[len(stack6)-1] + stack7[len(stack7)-1] + 
stack8[len(stack8)-1] + stack9[len(stack9)-1])