f = open("input.txt", "r")

def checkwin(correct, hand2check):
    wins = 0
    for i in correct:
        for hadn in hand2check:
            if i == hadn:
                wins += 1
    return wins

ans = 0
for line in f:
    game_data = line.strip().split('|')

    winningNums = game_data[0].split(': ')[1].strip().split()
    myNums = game_data[1].strip().split()
    ans += checkwin(winningNums, myNums)
print(ans)
