f = open("input.txt", "r")

red_limit = 12
green_limit = 13
blue_limit = 14
ans = 0

for line in f:
    gameNr, game = line.split(": ")
    valid_game = True

    for set in game.split("; "):
        cubes = set.split(", ")
        for cube in cubes:
            quantity, color = cube.split()
            if color == 'red' and int(quantity) > red_limit:
                valid_game = False
            elif color == 'green' and int(quantity) > green_limit:
                valid_game = False
            elif color == 'blue' and int(quantity) > blue_limit:
                valid_game = False

    if valid_game:
        number = int(gameNr.split()[1])
        ans += number
print(ans)

#for line in f:
#    gameNr, game = line.split(": ")
#    red_count = 0
#    green_count = 0
#    blue_count = 0
#    for set in game.split("; "):
#        print(set)
#        cubes = set.split(", ")
#        for cube in cubes:
#            quantity, color = cube.split()
#            if color == 'red':
#                red_count += int(quantity)
#            elif color == 'green':
#                green_count += int(quantity)
#            elif color == 'blue':
#                blue_count += int(quantity)
#
#    if red_count <= red_limit and green_count <= green_limit and blue_count <= blue_limit:
#        print(f"{gameNr} is valid.")
#        number = int(gameNr.split()[1])
#        ans += number
#print(ans)