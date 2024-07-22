import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

time = total = 0
h = m

if m + T > M:
  print(-1)
else:
  while time < N:
    if h + T <= M:
      h += T
      time += 1
      total += 1
      
    else:
      h -= R
      if h < m:
        h = m
      total += 1
  print(total)