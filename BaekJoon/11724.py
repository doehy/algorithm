import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

data =  [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(start,data,visited):
    visited[start] = 1
    for i in data[start]:
        if visited[i] == 0:
            dfs(i,data,visited)

result = 0


for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i,data,visited)
        result += 1

print(result)