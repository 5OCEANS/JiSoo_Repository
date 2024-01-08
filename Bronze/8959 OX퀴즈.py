n = int(input())

for i in range(n):
    q = list(input())
    s = 0
    rs = 0
    for j in q:
        if j =="O":
            s +=1
            rs +=s
        else:
            s = 0
    print(rs)
