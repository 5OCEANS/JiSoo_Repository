import sys

n = int(input())
a = []

for i in range(n):
    d = list(sys.stdin.readline().rstrip().split())
    a.append((d[0], int(d[1]), int(d[2]), int(d[3])))

k = sorted(a, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in k:
    print(j[0])