n = int(input())
l = len(n)
c = 0

if l > 1:
    i=0
    for i in range(1, l):
        c += 9 * (10 ** (i-1)) * i
    n = int(n) - (10 ** i)
    n += 1
    c += n * (i+1)
else:
    c = n

print(c)