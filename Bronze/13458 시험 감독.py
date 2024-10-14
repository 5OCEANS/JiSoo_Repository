n = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())

c = n
for i in l:
  i -= a
  if i > 0:
    if i % b:
      c += (i // b) + 1
    else:
      c += (i // b)

print(c)