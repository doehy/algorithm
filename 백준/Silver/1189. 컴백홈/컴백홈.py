n,m,k = map(int,input().split())
k -= 1

data = [list(input()) for _ in range(n)]

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(r,c,count,visited):
    global result
    if r == 0 and c == m-1:
        if count == k:
            result += 1
        return
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != "T" and not visited[nx][ny]:
            visited[r][c] = 1
            dfs(nx,ny,count+1,visited)
            visited[r][c] = 0

visited = [[0] * m for _ in range(n)]
dfs(n-1,0,0,visited)
print(result)