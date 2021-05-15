n = int(input())
N = [0, 1]
for i in range(2, n+1):
    X = N[i-1] + N[i-2]
    N.append(X)
print(N)