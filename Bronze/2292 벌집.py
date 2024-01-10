n = int(input())
s = 1
d = 6
room = 1

if n == 1:
    print(1)
else:
    while(1):
        s = s + d
        room += 1
        if n <= s:
            print(room)
            break
        else:
            d +=6

