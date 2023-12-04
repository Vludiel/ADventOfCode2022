data = open('input.txt').read()
p1 = 0
for x in range(len(data)):
    if p1 == 4:
        print(x)
        break
    if data[x] != data[x+1] and data[x] != data[x+2] and data[x] != data[x+3]:
        p1 += 1
    else:
        p1 = 0
