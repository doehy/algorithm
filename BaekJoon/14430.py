import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
dp = [[0 for _ in range(m)] for _ in range(n)]
dx = [0,1] # 오른쪽 아래
dy = [1,0]
for i in range(n):
    for j in range(m):
        if i - 1 >=0 and j - 1 >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + data[i][j]
        elif i - 1 >= 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        else:
            dp[i][j] = dp[i][j-1] + data[i][j]
print(dp[n-1][m-1]) 