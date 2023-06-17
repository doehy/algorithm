from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
visited = [[0] * m for _ in range(n)]
def check(q):
    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
            count += 1
        for k in range(4):
            ddx, ddy = dx[k], dy[k]
            nx, ny = x + ddx, y + ddy
            while 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]: # 방문하지 않았었다면
                    count += 1
                    visited[nx][ny] = 1
                if data[nx][ny] == 9:
                    break
                if data[nx][ny] == 3:
                    ddx, ddy = -ddy, -ddx
                elif data[nx][ny] == 4:
                    ddx, ddy = ddy, ddx
                elif (data[nx][ny] == 1 and ddx == 0) or (data[nx][ny] == 2 and ddy == 0):
                    break
                nx += ddx
                ny += ddy
    return count

def findAircon():
    q = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j] == 9:
                q.append((i,j))
    return check(q)

print(findAircon())
