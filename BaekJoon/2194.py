from collections import deque
import sys
input = sys.stdin.readline

# 유닛이 움직일 수 있는지 판단하는 함수 구현
def check(x,y):
    for i in range(x, x+a):
        for j in range(y, y+b):
            if i < 0 or i > (n-1) or j < 0 or j > (m-1):
                return False
            if graph[i][j] == -1:
                return False
    return True
def bfs():
    q = deque()
    q.append(start)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        if [x,y] == end:
            print(graph[x][y])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > (n-1) or ny < 0 or ny >(m-1):
                continue
            if graph[nx][ny] != 0:
                continue
            if check(nx,ny):
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
    print(-1)
    return
n,m,a,b,k = map(int,input().split())

graph = [[0  for j in range(m)] for _ in range(n)]

for i in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1] = -1 

start = list(map(int,input().split()))
start[0] -= 1
start[1] -= 1
end = list(map(int,input().split()))
end[0] -= 1
end[1] -= 1
print(graph)
bfs()