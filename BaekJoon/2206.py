from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for i in range(n):
    row = list(input().rstrip())
    graph.append(row)
visited = [[[0]*2 for _ in range(m)] for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x,y,visit = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][visit]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 일단 범위안에 있어야겠지
                if graph[nx][ny] == '0' and visited[nx][ny][visit] == 0:
                    visited[nx][ny][visit] = visited[x][y][visit] + 1
                    q.append([nx,ny,visit])
                if graph[nx][ny] == '1' and visit == 0:
                    visited[nx][ny][visit+1] = visited[x][y][visit] + 1
                    q.append([nx,ny,visit+1])
    return -1
print(bfs())