n = int(input())

def sm(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return sm(num-1) + sm(num-2) + sm(num-3)

for i in range(n):
    num = int(input())
    print(sm(num))