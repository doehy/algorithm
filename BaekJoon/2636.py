import sys
from collections import deque
r,c = map(int,input().split())

data = []
for i in range(r):
    data.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(data,sr,sc,visited):
    cnt = 0
    visited[sr][sc] = 1
    q = deque()
    q.append((sr,sc))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0: # 일단 방문하지 않았으면서 2는 다시는 확인안해도되는 공기
                if data[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif data[nx][ny] == 1:
                    cnt += 1
                    data[nx][ny] = 0
                    visited[nx][ny] = 1 # 여기서 방문 처리를 안해주면 이번 차례에 변하면 안되는 치즈가 변해버린다.
                    # 그렇다면 매번 visited 리스트를 만들어줘야한다. 그 이유는 다음 차례에 이 공기는 방문을 해야하는 공기이기 때문에 0으로 돼있어야한다.
    return cnt

answer = 0
count = 0

while True:
    answer += 1
    visited = [[0] * c for i in range(r)]
    number = bfs(data,0,0,visited)
    if number == 0:
        print(answer-1)
        print(count)
        break
    count = number

