from collections import deque

N,M = map(int,input().split())

kx, ky = map(int,input().split())

enemy = []

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

for i in range(M):
    a,b = map(int,input().split())
    enemy.append([a-1,b-1])

def solve(visited):
    q = deque()
    q.append((kx-1,ky-1))
    visited[kx-1][ky-1] = 0
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

                
visited = [[-1] * N for _ in range(N)] 
solve(visited)

for i in range(M):
    print(visited[enemy[i][0]][enemy[i][1]], end=" ")



# N의 최대 크기가 500일 떄 250000인 것을 보고 시간초과가 날 것 같다는 느낌을 받긴 했다.
# 수학적 접근도 아니고 뭐지.... 평소대로 너비 탐색을 하면 시간초과인데....
# 하지만 원 큐에 재네들을 한 번에 잡아낸다면 아무리 25만이라도 아슬아슬하게 통과가 되지 않을까