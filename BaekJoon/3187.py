from collections import deque

r,c = map(int,input().split())

data = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    tk = 0
    tv = 0
    if data[i][j] == 'k':
        tk += 1
    else:
        tv += 1
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != '#' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))
                if data[nx][ny] == "k":
                    tk += 1
                if data[nx][ny] == "v":
                    tv += 1
    return tk,tv

k = 0
v = 0

for i in range(r):
    for j in range(c):
        if data[i][j] == 'k' or data[i][j] == 'v' :
            if visited[i][j] == False:
                temp_k,temp_v = bfs(i,j)
                if temp_k > temp_v:
                    k += temp_k
                else:
                    v += temp_v
print(k,v)