SB = 2000
MB = 1500
HB = 1000
B = [SB, MB, HB]
COKE = 800
SPRITE = 700
D = [COKE, SPRITE]

for i in range(0,2):
    cheapB = B[2]
    if B[i] < cheapB:
        cheapB = B[i]

for j in range(0,1):
    cheapD = D[1]
    if D[j] < cheapD:
        cheapD = D[j]

print(cheapB + cheapD - 50)