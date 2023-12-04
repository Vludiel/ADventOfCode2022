txt = open("input.txt", "r")
lista = []
ans = 0
for line in txt:
    line_sum = []

    for ch in line:
        if(ch.isdigit()):
            line_sum.append(int(ch))
    ans += line_sum[0]*10 + line_sum[-1]
    
print(ans)
