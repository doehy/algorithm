from collections import deque
n,k = map(int,input().split())
data = []
virus = []
for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j],i,j))
s,r_x,r_y = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(s,r_x,r_y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            num,x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if data[nx][ny] == 0:
                        data[nx][ny] = data[x][y]
                        q.append((data[nx][ny],nx,ny))
        count += 1
    return data[r_x-1][r_y-1]

virus.sort()
print(bfs(s,r_x,r_y))

