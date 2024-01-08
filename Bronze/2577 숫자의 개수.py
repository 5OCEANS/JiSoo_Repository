a = int(input())
b = int(input())
c = int(input())

re = list(str(a*b*c))

for i in range(10):
    print(re.count(str(i)))
