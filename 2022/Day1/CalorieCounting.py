import fileinput
i = 0
summa = 0
elfs = []
for line in fileinput.input(files ='input.txt'):
    if line == "\n":
        i += 1
        elfs.insert(i, summa)
        summa = 0
        continue
    summa += int(line)
elfs.sort()
print(max(elfs)) #Total amount of calories of the elf who was carrying the most.
print(sum(sorted((elfs)[-3:]))) #Total amount of calorioes of the top three elfs who was carrying most.