sn = int(input())
ln = int(input())

sl = []
for n in range(sn, ln+1):
    e = 0
    if n >1 :
        for i in range(2, n):
            if n % i == 0:
                e += 1
                break
        if e == 0:
            sl.append(n)

if len(sl) > 0:
    print(sum(sl))
    print(min(sl))
else:
    print(-1)