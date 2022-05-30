from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

def find_path(x,y):
    global result
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 
    while queue:
        p,q = queue.popleft()
        for i in range(4):
            nx = p + dx[i]
            ny = q + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'X':
                if graph[nx][ny] != 0:
                    if graph[nx][ny] == 'P':
                        result += 1
                        graph[nx][ny] = 0
                        queue.append((nx,ny))
                    else:
                        graph[nx][ny] = 0
                        queue.append((nx,ny))
                

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            find_path(i,j)

if result == 0:
    print('TT')
else:
    print(result)