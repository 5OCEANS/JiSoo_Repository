n = int(input())
sco = []
re = 0
sco = list(map(float, input().split()))
k = max(sco)
for i in range(n):
    sco[i] = sco[i]/k*100
    re +=sco[i]
print(re/n)
