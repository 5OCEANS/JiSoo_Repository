n = int(input())
r = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    r = sum(a) + i
    if r == n:
        print(i)
        break
    if i == n :
        print(0)