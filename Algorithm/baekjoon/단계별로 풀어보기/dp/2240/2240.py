
t, w = map(int, input().split())
forecast = []
for _ in range(t):
    forecast.append(int(input()))


dp = [[[0]*2 for _ in range(w+2)] for _ in range(t+1)]

if t == 1:
    res = 1

else:

    if forecast[0] == 1:
        dp[1][1][0] = 1
    else:
        dp[1][2][1] = 1
    res = -1
    for i in range(2, t+1):
        for j in range(1, w+2):
            if forecast[i-1] == 1:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1]) + 1
                dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j][1])
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1])
                dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j][1]) + 1
            res = max(dp[i][j][0], res)
            res = max(dp[i][j][1], res)
    #res = max(dp[t][w+1])
print(res)