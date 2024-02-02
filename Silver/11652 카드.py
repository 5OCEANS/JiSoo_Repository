n = int(input())
a = {}

for i in range(n):
    j = int(input())
    if j in a:
        a[j] += 1
    else:
        a[j] = 1
r = sorted(a.items(), key=lambda x : (-x[1], x[0]))
print(r[0][0])

