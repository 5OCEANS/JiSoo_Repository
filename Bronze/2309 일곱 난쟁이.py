a = []
for i in range(9):
    n = int(input())
    a.append(n)

b = 0
c = 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(a) - (a[i]+a[j]) == 100:
            b, c = a[i], a[j]
            break
a.remove(b)
a.remove(c)


a.sort()
for i in a:
    print(i)
