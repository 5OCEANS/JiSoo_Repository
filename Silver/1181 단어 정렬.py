# n = int(input())
# w = []
#
# for i in range(n):
#     w.append(input())
#
# set_w = list(set(w))
#
# sort_w = []
# for i in set_w:
#     sort_w.append((len(i), i))
#
# re = sorted(sort_w)
#
# for l_w, w in re:
#     print(w)
#

n = int(input())
ws = []

for i in range(n):
    w = input()
    if w not in ws:
        ws.append(w)

ws.sort()
ws.sort(key=len)

for i in ws:
    print(i)



