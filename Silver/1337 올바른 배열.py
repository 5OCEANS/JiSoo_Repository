n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = sorted(a)
t = []
for i in range(0, n):
    c = 0
    for j in range(s[i], s[i]+5):
        if j not in s:
            c += 1
    t.append(c)
print(min(t))