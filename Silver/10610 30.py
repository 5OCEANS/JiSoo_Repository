n = input()

if "0" not in n:
    print(-1)
else:
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    if s % 3 != 0:
        print(-1)
    else:
        sn = sorted(n, reverse=True)
        an = "".join(sn)
        print(an)