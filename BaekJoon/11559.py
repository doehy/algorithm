from collections import deque
import sys
input = sys.stdin.readline
graph = []
for _ in range(12):
    graph.append(list(input().rstrip()))
moves = [
    [-1,0],
    [1,0],
    [0,-1],
    [0,1]
]
answer = 0

def bfs(color,i,j):
    count = 1
    data = [[i,j]]
    visited = [[0] * 6 for _ in range(12)] # 매번 방문기록을 다시 세워줄 것이고
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == color: # 같은색깔인지
                if not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    data.append([nx,ny])
    if count >= 4:
        for r,c in data:
            graph[r][c] = '.'
        return 1
    return 0
    # 4보다 적으면 아무일도 일어나지 말아야지
def toDown(color, r,c):
    for i in range(r+1,12):
        if graph[i][c] != '.':
            graph[r][c] = '.'
            graph[i-1][c] = color           
            break
        if i == 11 and graph[i][c] == '.':
            graph[r][c] = '.'
            graph[i][c] = color
 
def toDownSort():
    for i in range(10,-1,-1):
        for j in range(6):
            toDown(graph[i][j], i, j)

while True:
    flag = 0
    for i in range(12-1,-1,-1):
        for j in range(6):
            if graph[i][j] != '.':
                flag += bfs(graph[i][j],i,j) 
    if flag == 0:
        break
    toDownSort()
    answer += 1
print(answer)

