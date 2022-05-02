from collections import deque

N,M = map(int,input().split())


graph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    graph.append(list(map(int,input())))

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    if graph[x][y] == 1:
        return False
    while queue:
        x,y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx,ny))

    return True

num = 0
for i in range(N):
    for j in range(M):
        if BFS(i,j) == True:
            num +=1

print(num)