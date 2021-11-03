import os

file_in = open('input.txt', 'r')
file = list()
t = 0
for i in file_in:
    file.append(i.split())
file_in.close()

for i in range(0, len(file)):
    for j in range(0, len(file[i])):
        file[i][j] = int(file[i][j])

file_out = open('output.txt', 'w')
for i in file:
    f = True
    dif = i[0] - i[1]
    for j in range(1, len(i)-1):
        if i[j] - i[j+1] != dif:
            f = False
    if f:
        for k in i:
            file_out.write(str(k) + ' ')
        file_out.write('\n')

print(file)
os.startfile('output.txt')
