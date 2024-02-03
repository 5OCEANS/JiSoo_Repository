n = int(input())
l = {}

for i in range(n):
    a = input()
    if a not in l:
        l[a] = 1
    else:
        l[a] += 1

t = max(l.values())
k = []

for a, n in l.items():
    if n == t:
        k.append(a)
print(sorted(k)[0])

