import sys
input = sys.stdin.readline
c,n = map(int,input().split())
data = []
for _ in range(n):
    money, person = map(int,input().split())
    data.append((money,person))
dp = [float("inf")] * (c+100)
dp[0] = 0
for m,p in data:
    for i in range(p,c+100):
        dp[i] = min(dp[i],dp[i-p] + m)

print(min(dp[c:]))