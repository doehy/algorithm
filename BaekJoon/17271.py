n,m = map(int,input().split())

ans = 0

dp = [1] * (n+1)

if n < m:
    print(1)
else:
    dp[m] = 2
    for i in range(m+1,n+1):
        dp[i] = (dp[i-1] + dp[i-m]) % 1000000007
    print(dp[n])
