n = int(input())
c,sum = 0,0
start, end = 0,0

while end<=n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        c+=1
        end+=1
        sum+=end
print(c)