import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
data_set = set(data)
for i in range(m):
    for j in range(i+1,m):
        data_set.add(data[i] + data[j])

dp = [float("inf")] * (n+1)
dp[0] = 0
for i in range(n+1):
    for k in data_set:
        if i + k > n: continue # n을 넘는 것은 어차피 만들 필요가 없다. 그러니까 넘어간다. 
        dp[i + k] = min(dp[i] + 1, dp[i+k])

if dp[n] == float("inf"):
    print(-1)
else:
    print(dp[n])