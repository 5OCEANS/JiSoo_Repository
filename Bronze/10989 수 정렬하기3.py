import sys
n = int(sys.stdin.readline())
a = [0]*10001

for i in range(n):
    d = int(sys.stdin.readline())
    a[d] += 1
for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)

