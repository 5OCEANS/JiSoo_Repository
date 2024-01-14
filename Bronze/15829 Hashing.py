r = 31
M = 1234567891

l = int(input())
m = input()
h = 0

for i in range(l):
    h += (ord(m[i])-96) * (r**i)

print(h % M)