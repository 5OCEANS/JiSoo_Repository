n = int(input())
a = list(map(int, input().split()))

a.sort()
c = 0

for i in range(1, n+1):
    c += sum(a[0:i])
print(c)