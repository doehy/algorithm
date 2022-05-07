from collections import deque

n,m = map(int,input().split())

array = []

for _ in range(n):
    array.append(list(input()))

visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,end,team):
    cnt = 0
    visited[start][end] = 0
    queue = deque()
    queue.append((start,end))
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if array[nx][ny] == team:
                    cnt += 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 0
    return (1 if cnt == 0 else cnt)

w = 0
b = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            if array[i][j] == "W":
                w += bfs(i,j,array[i][j]) ** 2
            else:
                b += bfs(i,j,array[i][j]) ** 2

print(w,b)
