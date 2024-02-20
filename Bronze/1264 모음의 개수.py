a = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input().rstrip().lower()

    if s == '#':
        break

    c = 0
    for i in s:
        if i in a:
            c += 1
    print(c)