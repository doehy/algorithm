import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 47
dp[1] = 1
dp[2] = 1
for i in range(3,46):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1], dp[n])
