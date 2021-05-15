T = int(input())
for i in range(T):
    a = int(input())
    b = int(input())
    if a > b:
        b_num = a
    else:
        b_num = b
    while True:
        if b_num % a == 0 and b_num % b == 0:
            print(b_num)
            break

        b_num += 1