from collections import deque

def af_bfs(i,j,row,col, number, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    af_visited = [[0] * col for _ in range(row)]
    q = deque()
    q.append((i,j))
    af_visited[i][j] = number
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < row and 0 <= ny < col and af_visited[nx][ny] == 0:   
                if maps[nx][ny] == 'O' or maps[nx][ny] == 'S' or maps[nx][ny] == 'L':
                    q.append((nx,ny))
                    af_visited[nx][ny] = af_visited[x][y] + 1
                if maps[nx][ny] == 'E':
                    print(af_visited)
                    return af_visited[x][y] + 1
    return 0

def be_bfs(i,j,row,col, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    be_visited = [[0] * col for _ in range(row)]
    q = deque()
    q.append((i,j))
    be_visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < row and 0 <= ny < col and be_visited[nx][ny] == 0:   
                if maps[nx][ny] == 'O' or maps[nx][ny] == 'E':
                    q.append((nx,ny))
                    be_visited[nx][ny] = be_visited[x][y] + 1
                if maps[nx][ny] == 'L':
                    return af_bfs(nx, ny, row, col, be_visited[x][y] + 1, maps) 
    return 0

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    for i in range(row):
        for j in range(col):
            if maps[i][j] == "S":
                answer = be_bfs(i,j,row,col, maps) - 1
    
    return answer