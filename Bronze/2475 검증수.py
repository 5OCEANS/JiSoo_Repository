a,b,c,d,e = map(int,input().split())

k = (a*a+b*b+c*c+d*d+e*e)%10
print(k)

n = list(map(int, input().split()))
t = 0
for i in n:
    t +=i*i
print(t%10)