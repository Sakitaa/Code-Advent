with open('Day_1/input.txt') as f:
    data = f.read().splitlines()

calories = []
sum = 0

for line in data:
    if line != '':
        sum += int(line)
    if line == '':
        calories.append(sum)
        sum = 0

calories.sort()
calories.reverse()

print("Top Calories:")
for i in range(0, 3):
    print(str(i) + ": " + str(calories[i]))
    sum += calories[i]

print("Total calories: " + str(sum))