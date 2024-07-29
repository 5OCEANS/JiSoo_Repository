n = int(input())
s = map(int, input().split())
p = [0]*101
r = 0

for i in s:
  if(p[i]==0):
    p[i] += 1
  else:
    r += 1

print(r)