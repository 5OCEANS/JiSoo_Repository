import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

idx = 0 
for b in book:
    while True:
        if b <= box[idx]:
            box[idx] -= b
            break

        idx += 1
print(sum(box))