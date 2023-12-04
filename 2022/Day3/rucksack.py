import string
comp1 = []; comp2 = []
summa = 0

def calc(i):
    if i.islower():
        return string.ascii_lowercase.index(i)+1
    if i.isupper():
        return string.ascii_uppercase.index(i)+27

#PART ONE
for line in open('input.txt'):
    first, second = line[0:len(line)//2], line[len(line)//2: len(line)]
    comp1.append(first)
    comp2.append(second)
for x, y in zip(comp1, comp2):
    for i in y:
        if x.__contains__(i):
            summa += calc(i)
            break
print(summa)
#PART TWO
X = [line for line in open('input.txt')]
summa = 0
i = 0
while i < len(X):
    for c in X[i]:
        if c in X[i+1] and c in X[i+2]:
            summa += calc(c)
            break
    i += 3
print(summa)