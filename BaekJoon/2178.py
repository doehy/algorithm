from collections import deque
n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
queue.append((0,0))
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if  0<= nx < n and 0<= ny < m and graph[nx][ny]== 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))

print(graph[n-1][m-1]) 