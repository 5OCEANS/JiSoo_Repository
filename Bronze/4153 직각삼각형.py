while(1):
    n = list(map(int, input().split()))

    if sum(n)==0:
        break
    m = max(n)
    n.remove(m)

    if m**2 == n[0]**2 + n[1]**2:
        print("right")
    else:
        print("wrong")