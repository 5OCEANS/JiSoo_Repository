import sys
input = sys.stdin.readline

n = int(input())
p = {}

for _ in range(n):
  a, b = input().split()
  if b == 'enter':
    p[a] = True
  else:
    del p[a]
    
name = sorted(p, reverse=True)

for a in name:
  print(a)
