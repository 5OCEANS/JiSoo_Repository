import math

n = int(input())
f = math.factorial(n)

m = list(str(f))
c = 0
for i in range(len(m)):
    if m[i] == '0':
        c += 1
    else:
        c = 0
print(c)
