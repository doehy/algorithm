import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (21)
dp[0] = 1
dp[1] = 1
dp[2] = 2
if n < 3:
    print(dp[n])
else:
    for i in range(3,n+1):
        if i % 2 == 0:
            dp[i] = dp[i-1] * 2 - (dp[i-4] + dp[i-5])
        else:
            dp[i] = dp[i-1] * 2
    print(dp[n])
