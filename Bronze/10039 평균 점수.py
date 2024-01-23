a = []

for i in range(5):
    a.append(int(input()))

r = []
for i in a:
    if i < 40:
        r.append(40)
    else:
        r.append(i)

av = sum(r) / len(r)
print(int(av))