
# 5557 의 쉬운 버전.

# s 를 주의하자 시작점 이라는 것을 기억하자.
n, s, m = map(int, input().split())

numbers = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        prev = dp[i-1][j]
        if prev == 0:
            continue
        if j + numbers[i-1] <= m:
            dp[i][j+numbers[i-1]] = 1
        if j - numbers[i-1] >= 0:
            dp[i][j-numbers[i-1]] = 1



idx = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        idx = i
        break
print(idx)