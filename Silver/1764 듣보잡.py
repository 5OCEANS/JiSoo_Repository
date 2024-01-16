n, m = map(int, input().split())
a = set()
b = set()

for i in range(n):
    a.add(input())
for i in range(m):
    b.add(input())

r = sorted(list(a & b)) # 교집합

print(len(r))

for i in r:
    print(i)

