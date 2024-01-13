t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    p = [i for i in range(1, n+1)] # 0층
    for j in range(k):
        for c in range(1, n):
            p[c] += p[c-1]
    print(p[-1])

