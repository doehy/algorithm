from collections import deque
n = int(input())
data = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
b_visited = [[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

def avg(i,j,color):
    global count
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    if data[nx][ny] == color: # 같은 컬러일 경우만 queue에 넣어서 반복하게 해줘
                        visited[nx][ny] = True # 여기 안에 있을 때만 방문처리를 해주면 매번 visited를 새 것으로 갈아줄 필요가 없다.
                        queue.append((nx,ny))
                        count += 1


def b_avg(i,j,color):
    queue = deque()
    queue.append((i,j))
    b_visited[i][j] = True
    if color == 'B':
        while queue:
            x,y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if b_visited[nx][ny] == False:
                        if data[nx][ny] == color: # 같은 컬러일 경우만 queue에 넣어서 반복하게 해줘
                            b_visited[nx][ny] = True # 여기 안에 있을 때만 방문처리를 해주면 매번 visited를 새 것으로 갈아줄 필요가 없다.
                            queue.append((nx,ny))
    elif color == 'G':
        while queue:
            x,y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if b_visited[nx][ny] == False:
                        if data[nx][ny] == color or data[nx][ny] == 'R': # 같은 컬러일 경우만 queue에 넣어서 반복하게 해줘
                            b_visited[nx][ny] = True # 여기 안에 있을 때만 방문처리를 해주면 매번 visited를 새 것으로 갈아줄 필요가 없다.
                            queue.append((nx,ny))
    else:
        while queue:
            x,y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if b_visited[nx][ny] == False:
                        if data[nx][ny] == color or data[nx][ny] == 'G': # 같은 컬러일 경우만 queue에 넣어서 반복하게 해줘
                            b_visited[nx][ny] = True # 여기 안에 있을 때만 방문처리를 해주면 매번 visited를 새 것으로 갈아줄 필요가 없다.
                            queue.append((nx,ny))

b_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            avg(i,j,data[i][j])
        if not b_visited[i][j]:
            b_avg(i,j,data[i][j])
            b_count += 1

print(n*n - count,b_count)