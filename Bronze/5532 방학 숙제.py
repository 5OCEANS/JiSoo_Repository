import math

l = int(input())
a, b, c, d = [int(input()) for i in range(4)]

if (math.ceil(a/c) > math.ceil(b/d)):
  print(l-math.ceil(a/c))
else:
  print(l-math.ceil(b/d))