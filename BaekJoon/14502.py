from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def check():
    global answer
    temp = deepcopy(graph)
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))
                cnt += 1
    answer = max(answer, n*m - (byrus_count + cnt + wall_count + 3))       

def backTracking(count):
    if count == 3:
        check()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] =1
                backTracking(count + 1)
                graph[i][j] =0

answer = 0
byrus_count = 0
wall_count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            byrus_count += 1
        elif graph[i][j] == 1:
            wall_count += 1
backTracking(0)
print(answer)
