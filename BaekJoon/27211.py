from collections import deque

n,m = map(int,input().split())

data = [list(map(int,input().split())) for i in range(n)]

visited = [[0] * m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    data[r][c] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = (x + dx[k]) % n
            ny = (y + dy[k]) % m
            if data[nx][ny] == 0 and visited[nx][ny] == 0:
                data[nx][ny] = 1
                visited[nx][ny] = 1
                q.append((nx,ny))
answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and data[i][j] == 0:
            check(i,j)
            answer += 1

print(answer)