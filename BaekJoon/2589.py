from collections import deque

r,c = map(int,input().split())

data = list()
for i in range(r):
    data.append(list(input()))
dx = [(-1,0),(1,0),(0,-1),(0,1)]
def solve(i,j,visited):
    count = 0
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k][0]
            ny = y + dx[k][1]
            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] == 'L':
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    count = visited[nx][ny]
    return count

result = 0
for i in range(r):
    for j in range(c):
        if data[i][j] == "L":
            visited = [[0] * c for _ in range(r)]
            result = max(result,solve(i,j,visited))

print(result-1)

# 보물이 묻혀 있을 곳을 찾는게 아니라 거리 상 가장 먼 곳을 찾는 것이다. 이게 왜 골드 5지 메모리 때문인가?
# 크기에 대해서 값을 최대로 갱신한다해도 visited 처리가 제대로 되지 않아서 결국 새로 만들어줘야 하는데 이 때 메모리 초과가 날 까?
# 최대 2500번 2500크기를 가지는 배열을 만드는데