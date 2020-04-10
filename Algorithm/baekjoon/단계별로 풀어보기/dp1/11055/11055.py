


n = int(input())

number = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = number[i]
    
    for j in range(i):
        if number[i] > number[j] and dp[i] < dp[j] + number[i]:
            dp[i] = dp[j] + number[i]
print(max(dp))