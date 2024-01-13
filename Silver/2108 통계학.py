import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

def mean(num):
    return round(sum(num)/len(num))
def median(num):
    num.sort()
    mid = num[len(num)//2]
    return mid
def mode(num):
    d = Counter(num)
    k = d.most_common()

    if len(num) > 1:
        if k[0][1] == k[1][1]:
            mod = k[1][0]
        else:
            mod = k[0][0]
    else:
        mod = k[0][0]
    return mod
def scope(num):
    return max(num) - min(num)

print(mean(a))
print(median(a))
print(mode(a))
print(scope(a))

