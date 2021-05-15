M, N = map(int, input().split())
ans = []
for i in range(M, N+1):
    if i == 2:
        ans.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                ans.append(i)
print(ans)