import sys

def roundup(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    a = []
    for i in range(n):
        a.append((int(sys.stdin.readline())))

    a.sort()
    b = roundup(n*0.15)

    print(roundup(sum(a[b:n-b])/len(a[b:n-b])))
