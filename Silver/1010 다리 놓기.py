from math import factorial

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    r = factorial(b) // (factorial(a)*factorial(b-a))
    print(r)