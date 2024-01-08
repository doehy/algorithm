import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = [[0 for _ in range(300)] for _ in range(300)]
dp = [[0 for _ in range(300)] for _ in range(300)]
for _ in range(n):
    x,y = map(int,input().split())
    data[x][y] = m - (x+y)
    if data[x][y] < 0:
        data[x][y] = 0

k = 0
for i in range(300):
    for j in range(300):
        dp[i][j] = data[i][j] + max(dp[i-1][j], dp[i][j-1])
        k = max(dp[i][j], k)

print(k)