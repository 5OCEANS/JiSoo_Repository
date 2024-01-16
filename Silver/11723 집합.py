import sys

n = int(sys.stdin.readline())
a = set()

for i in range(n):
    k = sys.stdin.readline().strip().split()

    if k[0] == 'add':
        a.add(int(k[1]))
    elif k[0] == 'remove':
        a.discard(int(k[1]))
    elif k[0] == 'check':
        if int(k[1]) in a:
            print(1)
        else:
            print(0)
    elif k[0] == 'toggle':
        if int(k[1]) in a:
            a.discard(int(k[1]))
        else:
            a.add(int(k[1]))
    elif k[0] == 'all':
        a = set([i for i in range(1, 21)])
    else:
        a = set()


