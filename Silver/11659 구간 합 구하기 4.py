import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
j = [0]
c = 0

for i in range(n):
  c += s[i]
  j.append(c) 
  
for i in range(m):
  a, b = map(int, input().split())
  print(j[b]-j[a-1]) # 누적합에서 두 원소의 차를 구해 그 구간의 합 구함
  