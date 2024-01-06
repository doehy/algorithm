import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        if i + data[i][j] < n:
            dp[i+data[i][j]][j] += dp[i][j]
        if j + data[i][j] < n:
            dp[i][j + data[i][j]] += dp[i][j]
