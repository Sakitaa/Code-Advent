with open('Day_5/test.txt') as f:
    test = f.read().splitlines()

#stack1 = []
#stack1.append('Z')
#stack1.append('N')
#
#stack2 = []
#stack2.append('M')
#stack2.append('C')
#stack2.append('D')
#
#stack3 = []
#stack3.append('P')

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

    if fromWhere == 1:
        fromWhere = stack1
    elif fromWhere == 2:
        fromWhere = stack2
    elif fromWhere == 3:
        fromWhere = stack3
    elif fromWhere == 4:
        fromWhere = stack4
    elif fromWhere == 5:
        fromWhere = stack5
    elif fromWhere == 6:
        fromWhere = stack6
    elif fromWhere == 7:
        fromWhere = stack7
    elif fromWhere == 8:
        fromWhere = stack8
    elif fromWhere == 9:
        fromWhere = stack9
    

    if toWhere == 1:
        toWhere = stack1
    elif toWhere == 2:
        toWhere = stack2
    elif toWhere == 3:
        toWhere = stack3
    elif toWhere == 4:
        toWhere = stack4
    elif toWhere == 5:
        toWhere = stack5
    elif toWhere == 6:
        toWhere = stack6
    elif toWhere == 7:
        toWhere = stack7
    elif toWhere == 8:
        toWhere = stack8
    elif toWhere == 9:
        toWhere = stack9


    for i in range(0, howMany):
        popped = fromWhere.pop()
        toWhere.append(popped)

    if int(line[3]) == 1:
        stack1 = fromWhere
    elif int(line[3]) == 2:
        stack2 = fromWhere
    elif int(line[3]) == 3:
        stack3 = fromWhere
    elif int(line[3]) == 4:
        stack4 = fromWhere
    elif int(line[3]) == 5:
        stack5 = fromWhere 
    elif int(line[3]) == 6:
        stack6 = fromWhere 
    elif int(line[3]) == 7:
        stack7 = fromWhere
    elif int(line[3]) == 8:
        stack8 = fromWhere
    elif int(line[3]) == 9:
        stack9 = fromWhere
    
    if int(line[5]) == 1:
        stack1 = toWhere
    elif int(line[5]) == 2:
        stack2 = toWhere
    elif int(line[5]) == 3:
        stack3 = toWhere
    elif int(line[5]) == 4:
        stack4 = toWhere
    elif int(line[5]) == 5:
        stack5 = toWhere
    elif int(line[5]) == 6:
        stack6 = toWhere
    elif int(line[5]) == 7:
        stack7 = toWhere
    elif int(line[5]) == 8:
        stack8 = toWhere
    elif int(line[5]) == 9:
        stack9 = toWhere
        

print("Top of each stack:", stack1[len(stack1)-1] + 
stack2[len(stack2)-1] + stack3[len(stack3)-1] + 
stack4[len(stack4)-1] + stack5[len(stack5)-1] + 
stack6[len(stack6)-1] + stack7[len(stack7)-1] + 
stack8[len(stack8)-1] + stack9[len(stack9)-1]) # TPGVQPFD is incorrect