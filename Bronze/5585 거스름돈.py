m = int(input())
c = 0

n = 1000 - m

c += n // 500
n = n % 500
c += n // 100
n = n % 100
c += n // 50
n = n % 50
c += n // 10
n = n % 10
c += n // 5
n = n % 5
c += n // 1

print(c)

