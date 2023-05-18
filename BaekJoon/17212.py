n = int(input())

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + 1
    if i - 2 > -1:
        dp[i] = min(dp[i],dp[i-2]+1)
    if i - 5 > -1:
        dp[i] = min(dp[i],dp[i-5]+1)    
    if i - 7 > -1:
        dp[i] = min(dp[i],dp[i-7]+1)
    

print(dp[n])