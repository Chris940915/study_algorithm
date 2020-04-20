
t = int(input())
res = []

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1

    for c in coins:
        for i in range(1, m+1):
            if i >= c:
                dp[i] += dp[i-c] 
    
    print(dp[m])

