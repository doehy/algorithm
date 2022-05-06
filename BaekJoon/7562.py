from collections import deque
t = int(input())

dx = [-2,-2,2,2,-1,-1,1,1]
dy = [1,-1,1,-1,-2,2,-2,2]

for _ in range(t):
    l = int(input())
    s_x,s_y = map(int,input().split())
    e_x,e_y = map(int,input().split())
    if s_x  == e_x and s_y == e_y:
        print(0)
        continue
    graph = [[0] * l for _ in range(l)]
    queue = deque()
    queue.append((s_x,s_y))
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    print(graph[e_x][e_y])