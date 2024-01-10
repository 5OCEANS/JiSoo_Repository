n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    r = 1 # 기본순위 1로 고정
    for j in range(n):
        if(a[i][0] < a[j][0] and a[i][1] < a[j][1]):
            r += 1
    print(r, end=' ')