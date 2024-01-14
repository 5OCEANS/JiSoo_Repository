n, m, B = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]
mt = 9999999999
h = 0

for i in range(257):
    bottom = 0
    top = 0
    for j in range(n): #가로
        for k in range(m): #세로
            if g[j][k] >= i: #블럭이 현재 높이보다 크면
                top += g[j][k] - i
            else:
                bottom += i - g[j][k]

    if bottom > top + B:
        continue

    t = bottom + (top*2)
    if t <= mt:
        mt = t
        h = i
print(mt, h)