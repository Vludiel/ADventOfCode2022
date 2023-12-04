import fileinput
opponent = []
me = []
draw = 3
win = 6
loss = 0

rock = 1
paper = 2
scissors = 3

points = 0

for line in fileinput.input(files ='input.txt'):
    a, b = line.split(" ", 1)
    opponent.append(a)
    me.append(b.replace("\n",""))
#               PART ONE 
for (my_hand, opponent_hand) in zip(me, opponent):                                     
    if opponent_hand == 'A' and my_hand == 'X':
        points += rock+draw
    if opponent_hand == 'A' and my_hand == 'Y':
        points += paper+win
    if opponent_hand == 'A' and my_hand == 'Z':
        points += scissors+loss

    if opponent_hand == 'B' and my_hand == 'X':
        points += rock+loss
    if opponent_hand == 'B' and my_hand == 'Y':
        points += paper+draw
    if opponent_hand == 'B' and my_hand == 'Z':
        points += scissors+win

    if opponent_hand == 'C' and my_hand == 'X':
        points += rock+win
    if opponent_hand == 'C' and my_hand == 'Y':
        points += paper+loss
    if opponent_hand == 'C' and my_hand == 'Z':
        points += scissors+draw
print("\nTotal points part one=")
print(points)
#               PART TWO
points = 0 
for (my_hand, opponent_hand) in zip(me, opponent):                                     
    if opponent_hand == 'A' and my_hand == 'X': # LOOSE
        points += scissors+loss
    if opponent_hand == 'A' and my_hand == 'Y': # DRAW
        points += rock+draw
    if opponent_hand == 'A' and my_hand == 'Z': # WIN
        points += paper+win

    if opponent_hand == 'B' and my_hand == 'X': # LOOSE
        points += rock+loss
    if opponent_hand == 'B' and my_hand == 'Y': # DRAW
        points += paper+draw
    if opponent_hand == 'B' and my_hand == 'Z': # WIN
        points += scissors+win

    if opponent_hand == 'C' and my_hand == 'X': # LOOSE
        points += paper+loss
    if opponent_hand == 'C' and my_hand == 'Y': # DRAW
        points += scissors+draw
    if opponent_hand == 'C' and my_hand == 'Z': # WIN
        points += rock+win

print("\nTotal points part two=")
print(points)