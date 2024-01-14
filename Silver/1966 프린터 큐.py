from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = deque(list(map(int, input().split())))
    c = 0

    while(a):
        b = max(a)
        f = a.popleft()
        m -= 1

        if b == f:
            c += 1
            if m < 0:
                print(c)
                break
        else:
            a.append(f)
            if m < 0:
                m = len(a) - 1