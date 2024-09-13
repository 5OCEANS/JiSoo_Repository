n = int(input())

s = [[0] * n for _ in range(n)]
d = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(5):
        for k in range(n):
            if d[i][j] == d[k][j]:
                s[i][k] = 1

answers = [0] * n
for idx, s in enumerate(s):
    answers[idx] = s.count(1)

def pA(answers):
    for i in range(n):
        if answers[i] == max(answers):
            print(i+1)
            return

pA(answers)