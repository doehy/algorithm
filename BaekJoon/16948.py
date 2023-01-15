from collections import deque

n = int(input())

sr,sc,er,ec = map(int,input().split())

data = [[-1] * n for _ in range(n)]
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    data[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == -1:
                data[nx][ny] = data[x][y] + 1
                q.append((nx,ny))
    return data[er][ec]

print(bfs(sr,sc))
