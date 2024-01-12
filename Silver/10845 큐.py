import sys
from collections import deque

n = int(input())
a = deque()

for i in range(n):
    l = sys.stdin.readline().split()

    if l[0] == 'push':
        a.append(int(l[1]))
    elif l[0] == 'pop':
        if a:
            print(a.popleft())
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(a))
    elif l[0] == 'empty':
        if a:
            print(0)
        else:
            print(1)
    elif l[0] == 'front':
        if a:
            print(a[0])
        else:
            print(-1)
    elif l[0] == 'back':
        if a:
            print(a[-1])
        else:
            print(-1)
