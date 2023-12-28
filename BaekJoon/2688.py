import sys
input = sys.stdin.readline
t = int(input())
dp = [[1] * 10 for _ in range(65)]
    
for i in range(1,65):
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] 
for _ in range(t):
    n = int(input())
    print(dp[n][9])