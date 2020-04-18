


n = int(input())

number = []

for _ in range(n):
    number.append(int(input()))

dp = [1] * n

for i in range(n):

    for j in range(i):
        if number[i] > number[j]:
            if dp[j] >= dp[i]:
                dp[i] = dp[j] + 1

print(n-max(dp))