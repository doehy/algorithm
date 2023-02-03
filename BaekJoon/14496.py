from collections import deque

a,b = map(int,input().split())
n,m = map(int,input().split())

data = [[] for _ in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())
    data[s].append(e)
    data[e].append(s)
# dfs로 하면 visited로 하기가 어렵고 bfs로 하면 count세는게 헷갈리네 일단 visited를 넣어보자

def check(st,visited):
    visited[st] = 0
    q = deque()
    q.append(st)
    while q: # 제일 먼저왔다는 것이 제일 최소로 왔다는 의미니까 그냥 그거 출력하면 된다.
        x = q.popleft()
        for node in data[x]:
            if visited[node] == float("inf"):
                visited[node] = min(visited[node],visited[x]+1)
                q.append(node)
        
    return visited[b]

visited = [float("inf") for _ in range(n+1)]
good = check(a,visited)
if good == float("inf"):
    print(-1)
else:
    print(good)

