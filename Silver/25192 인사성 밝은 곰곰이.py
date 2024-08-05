def f(n):
  g = set()
  c = 0
  for i in range(n):
    r = input()
    if r == 'ENTER':
      g.clear()
    elif r != 'ENTER':
      if r not in g:
        c += 1
        g.add(r)
  return c

n = int(input())
print(f(n))