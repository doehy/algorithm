#3987
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
direction = ['U','R','D','L']
for _ in range(n):
    graph.append(list(input().rstrip()))
PR, PC = map(int,input().split())
resultDir, resultCnt = 'undetermined', 0
dx = [-1,0,1,0] # 위 오른쪽 아래 왼쪽
dy = [0,1,0,-1]

def check(sx,se,dir):
    q = deque()
    q.append((sx,se,dir))
    visited = [[[0,[0 for _ in range(4)]] for _ in range(m)] for _ in range(n)]
    visited[sx][se][0] = 1
    while q:
        x,y,di = q.popleft()
        nx = x + dx[di]
        ny = y + dy[di]
        if not (0 <= nx < n and 0 <= ny < m) or graph[nx][ny] == 'C': # 범위 밖으로 나갔거나 블랙홀을 마주치면 멈춘다.
            return visited[x][y][0]
        if graph[nx][ny] == '.':
            visited[nx][ny][0] = visited[x][y][0] + 1
            q.append((nx,ny,di))
            continue
        if not visited[nx][ny][1][di]: # 같은 방향에 대해서 같은 행성을 마주친 적 없어
            visited[nx][ny][1][di] = 1 # 방문 처리를 먼저 해준다.
            if graph[nx][ny] == '/':
                if di == 0 or di == 2:
                    di = (di + 1) % 4
                else:
                    di = (di - 1) % 4
            else: 
                if di == 1 or di == 3:
                    di = (di + 1) % 4
                else:
                    di = (di - 1) % 4
            visited[nx][ny][0] = visited[x][y][0] + 1
            q.append((nx,ny,di))
        else: # 같은 방향에 대해서 같은 행성을 마주쳤어
            return float("inf")
    # 루프를 나와서 리턴해 줄 것은 없다.

for i in range(4):
    num = check(PR-1,PC-1,i)
    if num == float("inf"):
        resultCnt = "Voyager"
        resultDir = direction[i]
        break
    if num > resultCnt:
        resultCnt = num
        resultDir = direction[i]
    
print(resultDir)
print(resultCnt)

# 평지에서 방문했는지에 따라서 멈추는 것이 아니라 이미 같은 방문한 행성이라면 멈추고 Voyager를 출력한다.
# 그러면 방문 처리를 할 때 일반적으로 방문 처리를 하면 안 된다. 방향 처리도 해줘야 한다.