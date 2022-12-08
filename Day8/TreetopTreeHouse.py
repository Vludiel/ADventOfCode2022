
data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]
treesWithSight = len(lines[0]) + len(lines[len(lines) - 1]) + len(lines) * 2 - 4

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        tree = 0
        #LEFT
        for left in reversed(range(0, j)):
            if int(lines[i][left]) < int(lines[i][j]):
                if left == 0:
                    tree += 1                
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #RIGHT
        for right in range(j + 1, len(lines[i])):
            if int(lines[i][right]) < int(lines[i][j]):
                if right == len(lines[i]) - 1:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #UP
        for up in reversed(range(0, i)):
            if int(lines[up][j]) < int(lines[i][j]):
                if up == 0:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #DOWN
        for down in range(i + 1, len(lines)):
            if int(lines[down][j]) < int(lines[i][j]):
                if down == len(lines) - 1:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
print(treesWithSight)