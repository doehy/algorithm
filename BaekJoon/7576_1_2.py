from collections import deque

m,n = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

day = 0

def tomato(a,b):
    global day
    queue = deque()
    queue.append((a,b))
    while queue:
        day += 1
        number = len(queue)
        for _ in range(number):
            x,y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx <n and ny >=0 and ny <m and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx,ny))
                
                
                
for i in range(n): #이중루프를 돌면서
    for j in range(m):
        if graph[i][j] == 1:
            tomato(i,j)
            break
    if graph[i][j] == 1:
        break

print(day)
