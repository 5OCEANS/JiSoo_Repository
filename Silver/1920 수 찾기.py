n = int(input())
na = set(map(int, input().split()))
m = int(input())
ma = list(map(int, input().split()))

for i in ma:
    if i in na:
        print(1)
    else:
        print(0)