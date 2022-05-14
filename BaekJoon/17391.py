from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(1,graph[x][y]+1):
            nx = x + i
            if nx > n-1:
                nx = n-1
            if visited[nx][y] == 0:
                visited[nx][y] = visited[x][y] + 1
                queue.append((nx,y))
        for i in range(1,graph[x][y]+1):
            ny = y + i
            if ny > m-1:
                ny = m - 1
            if visited[x][ny] == 0:
                visited[x][ny] = visited[x][y] + 1
                queue.append((x,ny))

                
visited = [[0] * m for _ in range(n)]

bfs(0,0)

print(visited[n-1][m-1]-1)