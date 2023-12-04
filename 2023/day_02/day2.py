f = open("input.txt", "r")

red_limit = 12
green_limit = 13
blue_limit = 14
partOne = 0
partTwo = 0

for line in f:
    gameNr, game = line.split(": ")
    valid_game = True

    min_red = 0
    min_green = 0
    min_blue = 0

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
            
            if color == 'red':
                min_red = max(min_red, int(quantity))
            elif color == 'green':
                min_green = max(min_green, int(quantity))
            elif color == 'blue':
                min_blue = max(min_blue, int(quantity)) 

    if valid_game:
        number = int(gameNr.split()[1])
        partOne += number
    
    partTwo += min_red * min_green * min_blue

print(partOne)
print(partTwo)