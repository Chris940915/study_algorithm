import sys

input = sys.stdin.readline


a = input().rstrip()
b = input().rstrip()

n_a = len(a)
n_b = len(b)

dp = [[0]*(n_b+1) for _ in range(n_a+1)]
max_V = -1

for i in range(1, n_a+1):
    a_ = a[i]
    for j in range(1, n_b+1):
        b_ = b[j]
        if a_ == b_:
            dp[i][j] = dp[i-1][j-1] + 1
            max_V = max(dp[i][j], max_V)

if max_V == -1:
    print(0)
else:
    print(max_V)