import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    q= deque()
    while fire:
        q.append(fire.popleft())
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if (x == 0 or y == 0 or x == h - 1 or y == w - 1) \
                and graph[x][y] != '#' and graph[x][y] != '*':
            return print(visited[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if graph[x][y] == '*' and visited[x][y] ==0 and graph[nx][ny] =='.':
                graph[nx][ny] ='*'
                q.append((nx,ny))
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] =='.':
                visited[nx][ny] = visited[x][y] +1
                graph[nx][ny] = visited[x][y] +1
                q.append((nx,ny))

    return print('IMPOSSIBLE')

for _ in range(t):
    w,h = map(int,input().split())
    graph = [list(input().strip()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    fire = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@' : sx,sy = i,j
            if graph[i][j] == '*' : fire.append((i,j))
    graph[sx][sy] = 1
    visited[sx][sy] =1
    bfs(sx,sy)