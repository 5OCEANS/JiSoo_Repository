n, m = map(int, input().split())
sum = 0
a = list(map(int, input().split()))
b = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            t = a[i]+a[j]+a[k]
            if t > m:
                continue
            else:
                b.append(t)

print(max(b))
