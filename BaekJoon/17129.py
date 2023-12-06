from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
visited = [[-1] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
sr,sc = 0,0
def start():
    global sr,sc
    for i in range(n):
        temp = list(input())
        for j in range(m):
            if temp[j] == '2':
                sr,sc = i,j
        data.append(temp)
def solve(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != '1' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if data[nx][ny] == '3' or data[nx][ny] == '4' or data[nx][ny] == '5':
                    return visited[nx][ny]
                q.append((nx,ny))
    return 0

start()
ans = solve(sr,sc)
if ans == 0:
    print("NIE")
else:
    print("TAK")
    print(ans)