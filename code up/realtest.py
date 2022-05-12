from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,h):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        x,y = queue.popleft()    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] > h:
                queue.append((nx,ny))
                visited[nx][ny] = True

n = int(input())

count = 0
result = 0

graph = [list(map(int,input().split())) for _ in range(n)]

for h in range(0,max(max(graph))):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                count += 1
                bfs(i,j,h)
    result = max(result,count)

print(result)