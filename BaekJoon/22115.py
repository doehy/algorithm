import sys
input = sys.stdin.readline
n,k = map(int,input().split())
data = list(map(int,input().split()))

dp = [[float("inf") for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

data.sort()
for i in range(1, n+1):
    for j in range(1, k+1):
        if j - data[i-1] >= 0: # 현재 만드려고 하는 무게에서 현재 들고 있는 보석으로 만들 수 있는지... 제일 중요한 거 하나씩
            dp[i][j] = min(dp[i-1][j-data[i-1]]+1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][k] == float("inf"):
    print(-1)
else:
    print(dp[n][k])
