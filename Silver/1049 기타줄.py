n, m = map(int, input().split())
p = [] #패키지
s = [] #낱개


for _ in range(m):
  a, b = map(int, input().split())
  p.append(a)
  s.append(b)
  
mp = min(p)

a = 0
while n > 0:
  if n>= 6:
    ms = min(s)*6
    n -= 6
  else:
    ms = min(s)*n
    n -=  n
  if ms < mp:
    a += ms
  else:
    a += mp
    
print(a)