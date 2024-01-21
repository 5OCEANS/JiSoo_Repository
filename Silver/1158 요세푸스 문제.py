from collections import deque

n, m = map(int, input().split())

q = deque(list(k+1 for k in range(n)))
r = []
c = 0
while q:
    c += 1
    t = q.popleft()

    if c == m:
        r.append(t)
        c = 0
    else:
        q.append(t)

print('<', ', '.join(map(str, r)), '>', sep='')

