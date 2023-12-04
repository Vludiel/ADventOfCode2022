txt = open("input.txt", "r")
lista = []

for line in txt:
    line_sum = []

    for ch in line:
        if(ch.isdigit()):
            line_sum.append(ch)

    lista.append(line_sum)

    if(len(line_sum) < 2):
        var = line_sum[0]
        line_sum.append(var)

two_dig_list = [[num[0], num[-1]] for num in lista]
result_list = [pair[0] + pair[1] for pair in two_dig_list]
digits = [int(x) for x in result_list]

print(sum(digits))
