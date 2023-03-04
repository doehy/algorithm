n,m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

max_num = 0

def high_left(r,c,visited):
    if c + 1 == m or r + 1 == n:
        return False
    if visited[r][c] == 1 or visited[r][c+1] == 1 or visited[r+1][c] == 1:
        return False
    visited[r][c] = 1
    visited[r][c+1] = 1
    visited[r+1][c] = 1
    return True

def high_right(r,c,visited):
    if c -1 < 0 or r + 1 == n:
        return False
    if visited[r][c] == 1 or visited[r+1][c] == 1 or visited[r][c-1] == 1:
        return False
    visited[r][c] = 1
    visited[r+1][c] = 1
    visited[r][c-1] = 1
    return True

def low_left(r,c,visited):
    if c + 1 == m or r -1 < 0:
        return False
    if visited[r][c] == 1 or visited[r-1][c] == 1 or visited[r][c+1] == 1:
        return False
    visited[r][c] = 1
    visited[r-1][c] = 1
    visited[r][c+1] = 1
    return True

def low_right(r,c,visited):
    if c - 1 < 0 or r - 1 < 0:
        return False
    if visited[r][c] == 1 or visited[r-1][c] == 1 or visited[r][c-1] == 1:
        return False
    visited[r][c] = 1
    visited[r-1][c] = 1
    visited[r][c-1] = 1
    return True

def solve(x,y,visited,count):
    global max_num
    if y == m:
        y = 0
        x += 1
    if x == n:
        max_num = max(count,max_num)
        return
    if high_left(x,y,visited):
        solve(x,y+1,visited,count+ 2*data[x][y] + data[x][y+1] + data[x+1][y])
        visited[x][y] = 0
        visited[x][y+1] = 0
        visited[x+1][y] = 0

    if high_right(x,y,visited):
        solve(x,y+1,visited,count+2*data[x][y]+ data[x][y-1] + data[x+1][y])
        visited[x][y] = 0
        visited[x][y-1] = 0
        visited[x+1][y] = 0

    if low_right(x,y,visited):
        solve(x,y+1,visited,count+2*data[x][y] + data[x-1][y] + data[x][y-1])
        visited[x][y] = 0
        visited[x-1][y] = 0
        visited[x][y-1] = 0
    
    if low_left(x,y,visited):
        solve(x,y+1,visited,count+2*data[x][y] + data[x-1][y] + data[x][y+1])
        visited[x][y] = 0
        visited[x-1][y] = 0
        visited[x][y+1] = 0
    solve(x,y+1,visited,count)

visited = [[0] * m for _ in range(n)]
solve(0,0,visited,0)
print(max_num)