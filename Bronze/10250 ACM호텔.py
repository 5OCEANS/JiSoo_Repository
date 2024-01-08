t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = n % h
    d = (n // h) + 1
    if f == 0:
        d -= 1
        f = h
    print(f * 100 + d)