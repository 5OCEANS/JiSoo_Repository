from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

if n == 1:
    print(-1)
elif n == 2:
    print(1)
elif n == 3:
    print(-1)
elif n == 4:
    print(2)
else:
    d = [100000] * (n + 1)
    d[2] = 1
    d[4] = 2
    d[5] = 1

    for i in range(5, n+1):
        d[i] = min(d[i], d[i-2]+1, d[i-5]+1)

    print(-1 if d[n] == 100000 else d[i])