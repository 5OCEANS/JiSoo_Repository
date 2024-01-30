n = int(input())

ro = []
v = []
for i in range(n):
    ro.append(int(input()))
ro.sort(reverse=True)

for j in range(n):
    v.append(ro[j]*(j+1))
print(max(v))