N = int(input())
X = int(input())
A = list(map(int, input().split()))
a = []

for i in range(N):
    if A[i] < X:
        a.append(A[i])
print(a)