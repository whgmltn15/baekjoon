A, B, V = map(int, input().split())
H = 0
while V > 0:
    H = H + 1
    if A * H - B * (H - 1) >= V:
        break
    print(H)