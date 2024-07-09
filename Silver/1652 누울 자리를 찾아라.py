b = int(input())

a = []
h = 0
v = 0

for i in range(b):
  s = input()
  a.append(s)
  
for i in range(b):
  c1 = 0 # 임시 가로 카운트
  c2 = 0 # 임시 세로 카운트
  for j in range(b):
    if a[i][j] == '.': # 가로
      c1 += 1
    else:
      c1 = 0
    if c1 == 2: # 연속으로 짐이 없다면
      h += 1 # 진짜 가로
    
    if a[j][i] == '.': # 세로
      c2 += 1
    else:
      c2 = 0
    if c2 == 2:
      v += 1 # 진짜 세로

print(h, v)