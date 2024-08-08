a, b = map(int, input().split())

s = []

for i in range(b+1):
  for j in range(i):
    if b == len(s):
      break
    s.append(i)
print(sum(s[a-1:b]))