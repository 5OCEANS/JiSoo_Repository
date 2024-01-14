k, n = map(int, input().split())
a=[]

for i in range(k):
    a.append(int(input()))

start = 1
end = max(a)

while(start <= end):
    mid = (start + end) // 2
    c = 0
    for i in range(k):
        c += a[i] // mid
    if c >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)