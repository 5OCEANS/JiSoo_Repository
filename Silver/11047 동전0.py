n, k = map(int, input().split())
a = []
c = 0

for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for j in a:
    c += k // j
    k = k % j

print(c)


