# n = int(input())
#
# a = list(map(int, input().split()))
#
# print(min(a), max(a))

n = int(input())
m = list(map(int, input().split()))
max = m[0]
min = m[0]

for i in m[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)