n, r = map(int, input().split())
a = []

for i in range(n):
  a.append(list(map(int, input().split())))
a.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)
# 금은동 많은순 정렬

for i in range(n):
  if a[i][0] == r:
    c = i
for i in range(n):
  if a[c][1:]==a[i][1:]:
    print(i+1)
    break