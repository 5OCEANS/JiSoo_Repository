n = int(input())

a = []

for i in range(n):
    x,y = map(int,input().split())
    a.append([y,x])

n = sorted(a)

for y,x in n:
    print(x, y)