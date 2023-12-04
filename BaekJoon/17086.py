from collections import deque

n,m = map(int,input().split())

data = []

#상 하 좌 우 윗오대각 윗왼대각 아래오대각 아래왼대각
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]

for i in range(n):
    data.append(list(map(int,input().split())))

def check(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if data[nx][ny] == 1:
                    return visited[x][y]
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

visited = [[0] * m for i in range(n)]
rr = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            rr = max(check(i,j),rr)
            visited = [[0] * m for i in range(n)]
            

print(rr)