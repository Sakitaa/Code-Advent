with open('Day_2/input.txt') as f:
    data = f.read().splitlines()

score = 0

for line in data:
    if 'A' in line: # Rock
        if 'X' in line:
            score += 1 # +1 for choosing Rock
            score += 3 # +3 for Draw
        elif 'Y' in line:
            score += 2 # +2 for choosing Paper
            score += 6 # +6 for Win
        elif 'Z' in line:
            score += 3 # +3 for choosing Scissors
            score += 0 # +0 for Loss
    elif 'B' in line: # Paper
        if 'X' in line:
            score += 1 # +1 for choosing Rock
            score += 0 # +0 for Loss
        elif 'Y' in line:
            score += 2 # +2 for choosing Paper
            score += 3 # +3 for Draw
        elif 'Z' in line:
            score += 3 # +3 for choosing Scissors
            score += 6 # +6 for Win
    elif 'C' in line: #Scissors
        if 'X' in line:
            score += 1 # +1 for choosing Rock
            score += 6 # +6 for Win
        elif 'Y' in line:
            score += 2 # +2 for choosing Paper
            score += 0 # +0 for Loss
        elif 'Z' in line:
            score += 3 # +3 for choosing Scissors
            score += 3 # +3 for Draw

print("Part One")
print("Final score: " + str(score))

score = 0

for line in data:
    if 'A' in line: # Rock
        if 'X' in line: # Loss
            score += 3 # +3 for choosing Scissors
            score += 0 # +0 for Loss
        elif 'Y' in line: # Draw
            score += 1 # +1 for choosing Rock
            score += 3 # +3 for Draw
        elif 'Z' in line: # Win
            score += 2 # +2 for choosing Paper
            score += 6 # +6 for Win
    elif 'B' in line: # Paper
        if 'X' in line:# Loss
            score += 1 # +1 for choosing Rock
            score += 0 # +0 for Loss
        elif 'Y' in line: # Draw
            score += 2 # +2 for choosing Paper
            score += 3 # +3 for Draw
        elif 'Z' in line: # Win
            score += 3 # +3 for choosing Scissors
            score += 6 # +6 for Win
    elif 'C' in line: # Scissors
        if 'X' in line: # Loss
            score += 2 # +2 for choosing Paper
            score += 0 # +0 for Loss
        elif 'Y' in line: # Draw
            score += 3 # +3 for choosing Scissors
            score += 3 # +3 for Draw
        elif 'Z' in line: # Win
            score += 1 # +1 for choosing Rock
            score += 6 # +6 for Win

print("Part Two")
print("Final score: " + str(score))
