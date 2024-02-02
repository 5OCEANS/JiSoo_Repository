a = []
sa = []
for i in range(8):
    a.append(int(input()))

sa = sorted(a, reverse=True)
sa = sa[:5]

r = []
t = 0
for i in sa:
    r.append(a.index(i)+1)


r.sort()
t = sum(sa)
print(t)
print(*r)