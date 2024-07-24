import sys
input = sys.stdin.readline
def rr(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

for _ in range(int(input())):
  n = int(input())
  while 1:
    if rr(n):
      print(n)
      break
    n += 1