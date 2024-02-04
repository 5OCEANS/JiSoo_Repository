n = int(input())
a = list(map(int, input().split()))

k = sorted(list(set(a)))
d = {k[i] : i for i in range(len(k))}
for i in a:
    print(d[i], end=' ')