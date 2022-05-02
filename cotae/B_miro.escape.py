from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):
    graph.append(list(map(int,input())))

#상 하 좌 우
dx = [-1,+1,0,0]
dy = [0,0,-1,+1]

def BFS(x,y) :
    queue = deque()
    queue.append((x,y))
    if graph[x][y] == 0: #괴물이 살고 있을 경우는 리턴해버린다.
        return
    else: #지나갈수 있는 길인경우 1 인경우
        while queue: #큐에 값이 있는 동안은 계속 된다.
           
            x,y = queue.popleft()
            for i in range(4):
                nx = x  + dx[i]
                ny = y  + dy[i]
                if nx>=0 and nx<N and ny >= 0 and ny < M and graph[nx][ny] == 1:#즉 그래프 안에 있을경우이다.
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
            
    return graph[N-1][M-1]

number = BFS(0,0)
print(number)