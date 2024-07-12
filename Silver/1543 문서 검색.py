n1 = input()
n2 = input()

c = 0
re = 0

while len(n1) - c >= len(n2):
  if n1[c:c+len(n2)] == n2:
    re += 1
    c += len(n2)

  else:
    c += 1

print(re)