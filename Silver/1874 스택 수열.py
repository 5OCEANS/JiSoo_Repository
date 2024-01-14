n = int(input())
s = []
a = []
f = 0
c = 1

for i in range(n):
    num = int(input())
    while c <= num:
        s.append(c)
        a.append("+")
        c += 1

    if s[-1] == num:
        s.pop()
        a.append("-")
    else:
        print("NO")
        f = 1
        break

if f == 0:
    for i in a:
        print(i)