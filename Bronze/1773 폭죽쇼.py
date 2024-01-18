n, m = map(int,input().split())
a = [0]*(m+1)

for i in range(n):
    c = int(input())
    if c == 1:
        print(m)
        quit()
    for j in range(c, m+1, c):
        a[j] = 1
print(sum(a))




