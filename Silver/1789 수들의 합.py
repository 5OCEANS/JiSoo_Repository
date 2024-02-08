s = int(input())

t = 0
n = 1

while t+n <= s:
    t += n
    n += 1
print(n-1)