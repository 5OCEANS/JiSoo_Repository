import sys

w = list(map(str, sys.stdin.readline().rstrip("\n")))
res = []

for i in range(1, len(w) - 1):
    for j in range(i + 1, len(w)):
        first = w[:i] 
        second = w[i:j] 
        third = w[j:] 

        first.reverse()
        second.reverse()
        third.reverse()

        res.append("".join(first + second + third))

print(min(res))