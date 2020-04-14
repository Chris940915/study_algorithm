

a = input()
b = input()

na = len(a)
nb = len(b)
dp = [['']*(nb+1) for _ in range(na+1)]

def max(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

for i in range(1, na+1):
    a_ = a[i-1]
    for j in range(1, nb+1):
        b_ = b[j-1]
        if a_ == b_:
            dp[i][j] = dp[i-1][j-1] + a_
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(dp[na][nb]))
print(dp[na][nb])