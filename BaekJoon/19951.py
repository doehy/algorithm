n,m = map(int,input().split())
graph = list(map(int,input().split()))
dp = [0] * (n+1)
for i in range(m):
    a,b,k = map(int,input().split())
    dp[a-1] += k
    dp[b] += -k
i = 1
cur = dp[0]
while i < n:
    dp[i] += cur
    cur = dp[i]
    i += 1
for i in range(n):
    print(graph[i] + dp[i], end=' ')