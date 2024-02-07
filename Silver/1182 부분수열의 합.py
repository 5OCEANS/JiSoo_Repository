from itertools import combinations

n, s = map(int, input().split())

a = list(map(int, input().split()))
c = 0
for i in range(1, n+1):
    k = combinations(a, i)

    for j in k:
        if sum(j) == s:
            c += 1
print(c)