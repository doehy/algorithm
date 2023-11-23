import sys
n,m = map(int,input().split())
data = list(map(int,input().split()))
dp = [0] * (n+1)
dp[0], dp[1] = 0, data[0]
for i in range(1,n+1):
    dp[i] = dp[i-1] + data[i-1]
for _ in range(m):
    i,j = map(int,input().split())
    if i == j:
        print(data[i-1])
    else:
        print(dp[j] - dp[i-1])