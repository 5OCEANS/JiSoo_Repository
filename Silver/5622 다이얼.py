a = input().lower()
di = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

t = 0

for i in range(len(a)):
    for j in di:
        if a[i] in j:
            t += di.index(j) + 3
print(t)