#백준 2577
A = int(input())
B = int(input())
C = int(input())

total = A*B*C
print(total)

total = str(total)

temp = []

for i in range(10):
    temp.append(0)

for i in range(len(total)):
    # print(total[i])
    temp[int(total[i])] += 1
print(temp)