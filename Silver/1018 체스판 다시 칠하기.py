n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())

s=[]
for i in range(n-7):
    for j in range(m-7):
        fw = 0
        fb = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if a[k][l] != 'W':
                        fw += 1
                    if a[k][l] != 'B':
                        fb += 1
                else:
                    if a[k][l] != 'B':
                        fw += 1
                    if a[k][l] != 'W':
                        fb += 1
        s.append(fw)
        s.append(fb)
print(min(s))