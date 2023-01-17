from collections import deque

n = int(input())

data = list()

for i in range(n):
    data.append(list(map(int,input().split())))

flag = 0
visited = [[False] *  n for i in range(n)]

def bfs(x,y):
    global flag
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        dx = [data[x][y],0]
        dy = [0,data[x][y]]
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if data[nx][ny] == -1:
                    flag = 1
                    return
                queue.append((nx,ny))
                visited[nx][ny] = True

bfs(0,0)
if flag == 1:
    print("HaruHaru")
else:
    print("Hing")