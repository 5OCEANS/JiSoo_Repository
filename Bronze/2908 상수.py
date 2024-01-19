n, m = input().split()
a = list(n)
b = list(m)

a.reverse()
b.reverse()

x = int(a[0]+a[1]+a[2])
y = int(b[0]+b[1]+b[2])

if x > y:
    print(x)
else:
    print(y)

# n, m = input().split()
# n = int(n[::-1])
# m = int(m[::-1])
#
# if n > m:
# 	print(n)
# else:
# 	print(m)