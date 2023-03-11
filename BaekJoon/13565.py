from collections import deque

n,m = map(int,input().split())

data = [list(input()) for _ in range(n)]

flag = 0
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solve(i,j,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = 2
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == '0':
                if visited[nx][ny] == 0:        
                    visited[nx][ny] = 2
                    q.append((nx,ny))
    
for i in range(1):
    for j in range(m):
        if data[i][j] == '0' and visited[i][j] != 2:
            solve(i,j,visited)

for i in range(n-1,n-2,-1): 
    for j in range(m):
        if visited[i][j] == 2:
            print("YES")
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print("NO")


