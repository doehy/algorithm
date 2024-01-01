import sys
input = sys.stdin.readline
n = int(input())
dp = []
for _ in range(n):
    dp.append(float(input()))
for i in range(1,n):
    dp[i] = max(dp[i], dp[i-1]*dp[i])
print('%0.3f' %max(dp))