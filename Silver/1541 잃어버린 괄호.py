a = input().split("-")

s = 0

k = sum(map(int, a[0].split('+')))
if a[0] == '-':
    s -= k
else:
    s += k

for k in a[1:]:
    k = sum(map(int, (k.split('+'))))
    s -= k
print(s)
