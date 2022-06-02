n = int(input())
m = int(input())

data = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

result =  -1

def dfs(start,data,visited):
    global result
    result += 1
    visited[start] = 1
    for i in data[start]:
        if visited[i] == 0:
            dfs(i,data,visited)
    
dfs(1,data,visited)

print(result)