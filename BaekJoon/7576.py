from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = []
for _ in range(n*h):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0,-3,3]
dy = [0,0,-1,1,0,0]
day = 0


queue = deque()
for i in range(n*h): #이중루프를 돌면서
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
            
while queue:
    x,y = queue.popleft()
    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        if k < 2:
            temp = x // n #층을 봐
            if nx // n == temp: #층이 같다면     
                if 0<= nx <n and 0<=ny<m and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
        else:
            if 0<= nx <n and 0<=ny<m and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    day = graph[x][y]

flag = 0

for i in range(n*h): #이중루프를 돌면서
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1

if flag == 1:
    print(-1)
else:
    if graph[x][y] == 1:
        print(0)
    else:
        print(day-1)

print(graph)