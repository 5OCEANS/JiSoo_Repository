T = int(input())
t = {'kg': ['lb', 2.2046], 'lb': ['kg', 0.4536], 'l': ['g', 0.2642], 'g': ['l', 3.7854]}
answer = ""
for i in range(T):
    num, unit = input().split() 
    answer += str('{:.4f}'.format(round(float(num)*t[unit][1], 4))) + " " + t[unit][0] + "\n"
print(answer)