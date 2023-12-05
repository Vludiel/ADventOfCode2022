from collections import defaultdict
f = open("input.txt", "r")

def checkwin(correctCards, myCards):
    wins = 0
    for correctNum in correctCards:
        for myNum in myCards:
            if correctNum == myNum:
                if wins == 0:
                    wins = 1
                else:
                    wins *= 2

    return wins

D = defaultdict(int)
ans = 0
 
for i, line in enumerate(f):
    D[i] += 1
    game_data = line.strip().split('|')
    winningNums = game_data[0].split(': ')[1].strip().split() 
    myNums = game_data[1].strip().split()
    ans += checkwin(winningNums, myNums)

    #partTwo
    winsEachCard = len(set(winningNums) & set(myNums))
    #print(f"val: {winsEachCard}\nd[i]: {i}")
    for j in range(winsEachCard):
        D[i+1+j] += D[i]

print(ans)
print(sum(D.values()))