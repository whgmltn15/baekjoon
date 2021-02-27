n = int(input())
bag = 0
while True:
    if n % 5 == 0:
        total = bag + (n // 5)
        print(total)
        break

        n = n - 3
        total = total + 1

        if n == 0:
            break