import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_gram(i,j,number):
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((i,j))
    visited[i][j] = number
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1: 
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return visited[n-1][m-1]

def gram_bfs(i,j,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if data[nx][ny] == 0: 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                if data[nx][ny] == 2:
                    return get_gram(nx,ny,visited[x][y] + 1)
    return visited[n-1][m-1]

def bfs(i,j,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if data[nx][ny] != 1: 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))


min_result = float("inf")
visited = [[-1] * m for _ in range(n)]
bfs(0,0,visited)
min_result = min(min_result,visited[n-1][m-1])
visited = [[-1] * m for _ in range(n)]
min_result = min(min_result,gram_bfs(0,0,visited))
if min_result == -1 or min_result > t:
    print("Fail")
else:
    print(min_result)


# 두 가지 경우를 각각 구하면 시간초과가 날라나
# 예를 들어 그람을 구하지 않고 가는 경우와 그람을 구하고 가는 경우
# 미로의 크기가 꽤 크기 때문에 두 가지를 각각 구할경우 시간초고가 날 거다. 결국 한 번에 이동해야 하는데
# 너비우선탐색을 사용해 최대한 빠르게 가다가 그람을 만나면 그람을 통해 이동하고가 안돼 그 때 그놈이 그람이 만난애인지 어떻게 알아
