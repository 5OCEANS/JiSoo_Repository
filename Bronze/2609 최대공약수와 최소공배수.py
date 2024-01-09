import math
a,b = map(int, input().split())
#
# def gcd(a, b):
#     while b != 0:
#         r = a % b
#         a = b
#         b = r
#     return a
# print(gcd(a, b))
#
# def lcm(a, b):
#     lcm = (a * b) // gcd(a, b)
#     return lcm
# print(lcm(a, b))

print(math.gcd(a, b))
print(math.lcm(a,b))