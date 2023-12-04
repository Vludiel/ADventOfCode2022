nisse1 = []; nisse2 = []
p1 = 0; p2 = 0
for line in open('input.txt'):
    line1, line2 = line.strip().split(",")
    nisse1_x, nisse1_y = line1.split("-")
    nisse2_x, nisse2_y = line2.split("-")
    nisse1_x = int(nisse1_x)
    nisse1_y = int(nisse1_y)
    nisse2_x = int(nisse2_x)
    nisse2_y = int(nisse2_y)

    if nisse1_x >= nisse2_x and nisse1_y <= nisse2_y:
        p1 += 1
    elif nisse2_x >= nisse1_x and nisse2_y <= nisse1_y:
        p1 += 1
    
    if nisse1_x <= nisse2_x <= nisse1_y or nisse1_y >= nisse2_y >= nisse1_x:
        p2 += 1
    elif nisse2_x <= nisse1_x <= nisse2_y or nisse2_y >= nisse1_y >= nisse2_x:
        p2 += 1

print(p1)
print(p2)