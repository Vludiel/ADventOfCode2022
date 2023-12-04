p1 = []
arr1 = ['S', 'C', 'V', 'N']
arr2 = ['Z','M','J','H','N','S']
arr3 = ['M','C','T','G','J','N','D']
arr4 = ['T','D','F','J','W','R','M']
arr5 = ['P','F','H']
arr6 = ['C','T','Z','H','J']
arr7 = ['D','P','R','Q','F','S','L','Z']
arr8 = ['C','S','L','H','D','F','P','W']
arr9 = ['D','S','M','P','F','N','G','Z']
arr = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]

for line in open('input.txt'):
    line = line.split(" ")
    QUANT = int(line[1])
    while QUANT != 0:
        temp = arr[int(line[3]) - 1]
        temp2 = arr[int(line[5]) - 1]
        temp2.append(temp.pop())
        QUANT -= 1
for x in arr:
    tmp = len(x)
    p1.append(x[tmp-1])
print(p1)