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
