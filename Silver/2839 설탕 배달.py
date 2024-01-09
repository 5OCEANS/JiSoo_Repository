n = int(input())
c = 0
while(1):
    if(n % 5 == 0):
        c = c + n//5
        print(c)
        break
    else:
        n = n - 3
        c += 1
    if n < 0:
        print("-1")
        break
