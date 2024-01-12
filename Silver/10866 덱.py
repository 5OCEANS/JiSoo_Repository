import sys
from collections import deque

n = int(input())
c = deque()

for i in range(n):
    l = list(sys.stdin.readline().split())

    if l[0] == 'push_front':
        c.appendleft(l[1])
    elif l[0] == 'push_back':
        c.append(l[1])
    elif l[0] == 'pop_front':
        if len(c) == 0:
            print(-1)
        else:
            print(c.popleft())
    elif l[0] == 'pop_back':
        if len(c) == 0:
            print(-1)
        else:
            print(c.pop())
    elif l[0] == 'size':
        print(len(c))
    elif l[0] == 'empty':
        if len(c) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 'front':
        if len(c) == 0:
            print(-1)
        else:
            print(c[0])
    elif l[0] == 'back':
        if len(c) == 0:
            print(-1)
        else:
            print(c[-1])
