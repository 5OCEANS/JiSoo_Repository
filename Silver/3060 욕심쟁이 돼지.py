for _ in range(int(input())):
  n = int(input())
  f = sum(list(map(int, input().split())))
  d = 1
  while n >= f:
    d += 1
    f *= 4
  print(d)