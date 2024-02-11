b = []

for i in range(3):
    b.append(int(input()))

d = []

for i in range(2):
    d.append(int(input()))

ms = min(b) + min(d) - 50
print(ms)