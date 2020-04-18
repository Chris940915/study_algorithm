
n = int(input())

numbers = list(map(int, input().split()))

dp = [[0]*21 for _ in range(n-1)]

dp[0][numbers[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        prev = dp[i-1][j]

        if prev != 0:
            if j + numbers[i] <= 20:
                dp[i][j+numbers[i]] += prev
            
            if j - numbers[i] >= 0:
                dp[i][j-numbers[i]] += prev

print(dp[n-2][numbers[-1]])