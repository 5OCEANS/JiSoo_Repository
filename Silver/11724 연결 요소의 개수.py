import sys
input = sys.stdin.readline

n, m = map(int, input().split())
no = [list(map(int, input().split())) for _ in range(m)]
am = [[] for _ in range(n+1)]

for u, v in no:
    am[u].append(v)
    am[v].append(u)

c = 0
vi = [0] * (n+1)
def dfs(v):
    vi[v] = 1
    for i in am[v]:
        if not vi[i]:
            dfs(i)
for i in range(1, n+1):
    if not vi[i]:
        dfs(i)
        c += 1
print(c)