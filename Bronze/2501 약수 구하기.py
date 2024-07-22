n, t = map(int,input().split())
for i in range(1,n+1):
    if n % i == 0:
        t -= 1
    if t == 0:
        print(i)
        break
else:
    print(0)