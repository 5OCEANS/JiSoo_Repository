n = int(input())

for _ in range(n):
    m = list(map(str, input().split()))
    answer = 0
    for i in range(len(m)):
        if i == 0:
            answer += float(m[i])
        else:
            if m[i] == "#":
                answer -= 7
            elif m[i] == "%":
                answer += 5
            elif m[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)