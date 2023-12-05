f = open("input.txt", "r")

def checkwin(correct, hand2check):
    wins = 0
    for i in correct:
        for hand in hand2check:
            if i == hand:
                if wins == 0:
                    wins = 1
                else:
                    wins *= 2
    return wins

ans = 0
for line in f:
    game_data = line.strip().split('|')

    winningNums = game_data[0].split(': ')[1].strip().split()
    myNums = game_data[1].strip().split()
    ans += checkwin(winningNums, myNums)
print(ans)
