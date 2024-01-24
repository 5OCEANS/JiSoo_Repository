n = set(range(1, 10001))
m = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    m.add(i)
s = sorted(n - m)
for i in s:
    print(i)