b = input()
score = 10

for i in range(1, len(b)):
    if b[i-1] == b[i]:
        score += 5
    else:
        score += 10
print(score)