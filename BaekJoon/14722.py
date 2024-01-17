import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, -1] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        leftCheck = (dp[i][j-1][1]+1)%3 == data[i-1][j-1]
        upCheck = (dp[i-1][j][1]+1)%3 == data[i-1][j-1]

        leftMilk = dp[i][j-1][0] + leftCheck
        upMilk = dp[i-1][j][0] + upCheck

        if leftMilk > upMilk:
            dp[i][j][0] = leftMilk
            dp[i][j][1] = data[i-1][j-1] if leftCheck else dp[i][j-1][1]
        else:
            dp[i][j][0] = upMilk
            dp[i][j][1] = data[i-1][j-1] if upCheck else dp[i-1][j][1]

print(dp[n][n][0])


# 그냥 결국 왼쪽, 위와 비교해서 더 큰것을 가져온다