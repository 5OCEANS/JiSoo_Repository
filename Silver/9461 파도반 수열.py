# 1 1 1 2 2 3 4 5 7 9
# P(n) = P(n-2) + P(n-3)

m = int(input())

a = [0] * 101
a[1] = 1
a[2] = 1
a[3] = 1

for i in range(4, 101):
    a[i] = a[i-2] + a[i-3]

for i in range(m):
    n = int(input())
    print(a[n])