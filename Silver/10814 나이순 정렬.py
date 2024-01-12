n = int(input())
l = []

for i in range(n):
    a, n = map(str, input().split())
    a = int(a)
    l.append((a, n))

l.sort(key = lambda x : x[0]) # (age, name) 에서 age만 비교

for i in l:
    print(i[0], i[1])