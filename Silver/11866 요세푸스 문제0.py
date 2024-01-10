from collections import deque

n, k = map(int, input().split())
a = deque()

for i in range(1, n+1):
    a.append(i)

print("<", end='')

while(a):
    for i in range(k-1):
        a.append(a.popleft())
    print(a.popleft(), end='')
    if a:
        print(", ",end='')
print(">")

