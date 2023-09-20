# 17073 나무 위의 빗물
import sys
input = sys.stdin.readline
n, w = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
for i in range(2,n+1):
    if len(graph[i]) == 1:
        cnt += 1
result = w / cnt
print(result)