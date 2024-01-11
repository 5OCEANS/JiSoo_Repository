from collections import Counter

n = int(input())
nl = list(map(int,input().split()))
m = int(input())
ml = list(map(int,input().split()))

c = Counter(nl)

for i in range(len(ml)):
    if ml[i] in c:
        print(c[ml[i]], end=' ')
    else:
        print(0, end=' ')