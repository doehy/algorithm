import sys
input = sys.stdin.readline
d,m = map(int,input().split())
dp = [[0] * 4001 for _ in range(4001)]
dp[1][1] = 1
for i in range(2,d): # d-1 까지만 가는 이유 마지막 d일때는 그냥 직전 위치 높이 1에서 내려오는 방법밖에 없으니
    for j in range(1,i+1): # 해당 좌표까지는 해당 높이까지만 올라갈 수 있으므로 i+1까지 가준다. 1부터시작해야지
        dp[i][j] += (dp[i-1][j-1] + dp[i-1][j+1]) % m
print(dp[d-1][1])
        