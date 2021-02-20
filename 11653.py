n = int(input())
temp = 2
while n != 1:
    for i in range(n):
        flag = 0
        if n % temp == 0:
            n = n//temp
            print(temp)
        else:
            temp += 1