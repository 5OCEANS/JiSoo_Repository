n, m, v = map(int, input().split())

g = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = g[b][a] = 1

visit = [0] * (n+1)

def dfs(v):
    visit[v] = 1 # 방문한 점 1
    print(v, end=" ")
    for i in range(1, n+1):
        if (visit[i]==0) and (g[v][i]==1):
            dfs(i)

def bfs(v):
    q = [v]
    visit[v] = 0 # 방문한 점 0
    while q:
        v = q.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if (visit[i]==1) and (g[v][i]==1):
                q.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)
