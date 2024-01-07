s = int(input())
for i in range(s):
    k, w = input().split()
    for j in w:
        print(j*int(k), end='')
    print()