N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
min_num = float("inf")

def one_cctv(r,c,visited,flag):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    while True:
        nx = r + dx[flag]
        ny = c + dy[flag]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                break
            if visited[nx][ny] <= 0:
                visited[nx][ny] -= 1
            r,c = nx,ny
        else:
            break

def one_cctv_clear(r,c,visited,flag):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    while True:
        nx = r + dx[flag]
        ny = c + dy[flag]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                break
            if visited[nx][ny] < 0:
                visited[nx][ny] += 1
            r,c = nx,ny
        else:
            break

def two_cctv(r,c,visited,flag):
    dx = [(0,0), (-1,1)]
    dy = [(-1,1), (0,0)]
    tr,tc = r,c
    for i in range(2):
        r,c = tr,tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M: # 계쏙 범위 안에 있나
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r,c = nx,ny
            else:
                break # 계속 더하기 때문에 범위 안에 계속 있을 수가 없어 

def two_cctv_clear(r,c,visited,flag):
    dx = [(0,0), (-1,1)]
    dy = [(-1,1), (0,0)]
    tr,tc = r,c
    for i in range(2):
        r,c = tr,tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r,c = nx,ny
            else:
                break

def three_cctv(r,c,visited,flag):
    dx = [(-1,0), (0,1), (1,0), (0,-1)]
    dy = [(0,1), (1,0), (0,-1), (-1,0)]
    tr,tc = r,c
    for i in range(2):
        r,c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r,c = nx,ny
            else:
                break

def three_cctv_clear(r,c,visited,flag):
    dx = [(-1,0), (0,1), (1,0), (0,-1)]
    dy = [(0,1), (1,0), (0,-1), (-1,0)]
    tr,tc = r, c
    for i in range(2):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r,c = nx,ny
            else:
                break

def four_cctv(r,c,visited,flag):
    dx = [(0,-1,0), (-1,0,1), (0,1,0), (1,0,-1)]
    dy = [(-1,0,1), (0,1,0), (1,0,-1), (0,-1,0)]
    tr, tc = r, c
    for i in range(3):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r,c = nx,ny
            else:
                break

def four_cctv_clear(r,c,visited,flag):
    dx = [(0,-1,0), (-1,0,1), (0,1,0), (1,0,-1)]
    dy = [(-1,0,1), (0,1,0), (1,0,-1), (0,-1,0)]
    tr, tc = r ,c
    for i in range(3):
        r,c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r,c = nx,ny
            else:
                break

def five_cctv(r,c,visited,flag):
    dx = [(0,-1,0,1)]
    dy = [(-1,0,1,0)]
    tr, tc = r, c
    for i in range(4):
        r,c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r,c = nx,ny
            else:
                break

def five_cctv_clear(r,c,visited,flag):
    dx = [(0,-1,0,1)]
    dy = [(-1,0,1,0)]
    tr,tc = r, c
    for i in range(4):
        r,c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6: # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r,c = nx,ny
            else:
                break

def solve(r,c,data):
    global min_num
    if c == M:
        c = 0
        r += 1
    if r == N:
        count = 0
        for i in range(N):
            for j in range(M):
                if data[i][j] == 0:
                    count += 1
        min_num = min(min_num,count)
        return
    if 1 <= data[r][c] <= 5:       
        if data[r][c] == 1:
            one_cctv(r,c,data,0)
            solve(r,c+1,data)
            one_cctv_clear(r,c,data,0)
            one_cctv(r,c,data,1)
            solve(r,c+1,data)
            one_cctv_clear(r,c,data,1)
            one_cctv(r,c,data,2)
            solve(r,c+1,data)
            one_cctv_clear(r,c,data,2)
            one_cctv(r,c,data,3)
            solve(r,c+1,data)
            one_cctv_clear(r,c,data,3)
        if data[r][c] == 2:
            two_cctv(r,c,data,0)
            solve(r,c+1,data)
            two_cctv_clear(r,c,data,0)
            two_cctv(r,c,data,1)
            solve(r,c+1,data)
            two_cctv_clear(r,c,data,1)
        if data[r][c] == 3:
            three_cctv(r,c,data,0)
            solve(r,c+1,data)
            three_cctv_clear(r,c,data,0)
            three_cctv(r,c,data,1)
            solve(r,c+1,data)
            three_cctv_clear(r,c,data,1)
            three_cctv(r,c,data,2)
            solve(r,c+1,data)
            three_cctv_clear(r,c,data,2)
            three_cctv(r,c,data,3)
            solve(r,c+1,data)
            three_cctv_clear(r,c,data,3)
        if data[r][c] == 4:
            four_cctv(r,c,data,0)
            solve(r,c+1,data)
            four_cctv_clear(r,c,data,0)
            four_cctv(r,c,data,1)
            solve(r,c+1,data)
            four_cctv_clear(r,c,data,1)
            four_cctv(r,c,data,2)
            solve(r,c+1,data)
            four_cctv_clear(r,c,data,2)
            four_cctv(r,c,data,3)
            solve(r,c+1,data)
            four_cctv_clear(r,c,data,3)
        if data[r][c] == 5:
            five_cctv(r,c,data,0)
            solve(r,c+1,data)
            five_cctv_clear(r,c,data,0)
    else:
        solve(r,c+1,data)
    
solve(0,0,data)
print(min_num)

# 처음의 감시 카메라의 위치들을 다 구해놓은 다음에 애내들을 다 90도 방향으로 돌리면 되지 않음?????
# 다 90도를 돌려가면서 확인을 해야 된다. 
# 3,4가 문제다 재귀가 잘 안되니 저렇게 나오는 것이다.