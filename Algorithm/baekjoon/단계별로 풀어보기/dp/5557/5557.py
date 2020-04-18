


n = int(input())
number = list(map(int, input().split()))

dp1 = [0]*21
dp2 = [0]*21

dp1[number[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if j + number[i] <= 20:
            dp2[j+number[i]] += dp1[j]
        if j - number[i] >= 0:
            dp2[j-number[i]] += dp1[j]
    
    dp1 = dp2
    dp2 = [0]*21

print(dp1[number[-1]])