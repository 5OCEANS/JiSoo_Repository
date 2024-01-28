import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dic_n = {}
dic_s = {}
for i in range(n):
    v = input().strip()
    dic_n[str(i+1)] = v
    dic_s[v] = i+1

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(dic_n[q])
    if q.isalpha():
        print(dic_s[q])
