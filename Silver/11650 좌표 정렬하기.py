n = int(input())

l = []
for i in range(n):
    [x, y] = map(int, input().split())
    l.append([x, y])

sa = sorted(l)
for i in range(n):
    print(sa[i][0], sa[i][1])