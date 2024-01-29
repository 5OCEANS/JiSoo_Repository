n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = [0] * (n)

if len(a) <= 2:
    print(sum(a))
else:
    d[0] = a[0]
    d[1] = a[0] + a[1]
    for i in range(2, n):
        d[i] = max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i])
    print(d[-1])

