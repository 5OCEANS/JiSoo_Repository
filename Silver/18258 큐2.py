import sys
from collections import deque

n = int(input())
q = deque()

for i in range(n):
    c = list(map(str, sys.stdin.readline().split()))
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if q:
            print(q[0])
        else:
            print("-1")
    elif c[0] == 'back':
        if q:
            print(q[-1])
        else:
            print("-1")
