import sys

n = int(input())
nl = set(map(int, sys.stdin.readline().split()))

m = int(input())
ml = list(map(int, sys.stdin.readline().split()))

for i in ml:
    if i in nl:
        print("1", end=" ")
    else:
        print("0", end=" ")