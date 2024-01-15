n = int(input())
a = [0] * (n+1) # n만큼 초기화

for i in range(2, n+1): # 1은 횟수가 0이니까 2부터 탐색
    a[i] = a[i-1] + 1 # 기본 값으로 이전 항의 연산 횟수 + 1

    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1) # 미리 저장해 둔 값과 몫+1 한 값 중 더 작은 값

print(a[n])
