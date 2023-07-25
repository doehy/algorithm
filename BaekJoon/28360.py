import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v,w = map(int,input().split())
    graph[v].append(w)
dp = [0] * (n+1)
dp[1] = 100
answer = []
for i in range(1,n+1):
    if len(graph[i]) > 0:
        for j in graph[i]:
            dp[j] += dp[i] / len(graph[i])
    else:
        answer.append(dp[i])
print(max(answer))

