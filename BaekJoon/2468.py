from collections import deque

n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(start,end,height):
    queue = deque()
    queue.append((start,end))
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 0:
                queue.append()


result = 0

graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(1,max(max(graph))+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                bfs(i,j,k)
    result = max(result,count(graph))
    



