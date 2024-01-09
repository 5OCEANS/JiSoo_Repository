n = int(input())
m = list(map(int, input().split()))

r = []
for i in range(n):
    if m[i] == 1:
        continue
    else:
        k = m[i]
        c = 0
        for j in range(2, k):
            if k % j == 0:
                c += 1
        if c == 0:
            r.append(k)
print(len(r))

