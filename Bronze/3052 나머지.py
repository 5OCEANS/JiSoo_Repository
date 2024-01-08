n=[]
for i in range(10):
    a = int(input())
    b = a%42
    n.append(b)
r = set(n)
print(len(r))

n = []
for i in range(10):
    a = int(input())
    if a%42 not in n:
        n.append(a%42)
print(len(n))