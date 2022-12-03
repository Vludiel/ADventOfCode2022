import fileinput
import string
comp1 = []; comp2 = []
summa = 0
for line in fileinput.input(files ='input.txt'):
    first, second = line[0:len(line)//2], line[len(line)//2: len(line)]
    comp1.append(first)
    comp2.append(second)
for x, y in zip(comp1, comp2):
    for i in y:
        if x.__contains__(i):
            if i.islower():
                summa += string.ascii_lowercase.index(i)+1
                break
            if i.isupper():
                summa += string.ascii_uppercase.index(i)+27
                break
print(summa)