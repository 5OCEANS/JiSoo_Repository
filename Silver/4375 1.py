import sys
input = sys.stdin.read

for i in map(int, input().split()):
  n = 1
  while 1:
    if n % i == 0:
      print(len(str(n)))
      break
  
    n *= 10
    n += 1