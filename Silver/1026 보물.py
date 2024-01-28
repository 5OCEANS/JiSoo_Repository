# n = int(input())
#
# al = list(map(int, input().split()))
# bl = list(map(int, input().split()))
#
# sa = sorted(al, reverse=True)
# sb = sorted(bl)
#
# c = 0
# for i in range(n):
#     c += sa[i] * sb[i]
# print(c)

n = int(input())

al = list(map(int, input().split()))
bl = list(map(int, input().split()))

c = 0
for i in range(n):
    c += min(al) * max(bl)
    al.pop(al.index(min(al)))
    bl.pop(bl.index(max(bl)))

print(c)