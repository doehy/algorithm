dp = [0 for _ in range(50001)]
dp[1], dp[2], dp[3] = 1, 1, 2
N = int(input())
if N <= 3:
    print(dp[N])
else:
    for i in range(4, N+1):
        dp[i] = (dp[i-1] + dp[i-3]) % 1000000009
    print(dp[N])