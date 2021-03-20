testCase = int(input())
for i in range(testCase):
    OX = input()
    score = 0
    count = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            count += 1
            score += count
        elif OX[j] == 'X':
            score += 0
            count = 0

    print(score)