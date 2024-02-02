n = int(input())

def siri(a):
    r = 0
    for i in a:
        if i.isdigit():
            r += int(i)
    return r
ser = [input().rstrip() for _ in range(n)]
ser.sort(key = lambda x:(len(x), siri(x), x))
for j in ser:
    print(j)