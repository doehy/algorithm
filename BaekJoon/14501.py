import sys
input = sys.stdin.readline

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

dp = [0] * (n+1)

for i in range(n-1,-1,-1):
    if i + data[i][0] <= n:
        dp[i] = max(dp[i+1],data[i][1]+dp[i+data[i][0]])
    else:
        dp[i] = dp[i+1]

print(dp[0])
