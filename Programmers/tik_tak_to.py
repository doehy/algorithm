from collections import deque

def o_check(board, dx, i, j): #밑으로만 쭉
    flag = 0
    q = deque()
    for k in range(4):
        visited = [[0] * 3 for _ in range(3)]
        q.append((i,j))
        visited[i][j] = 1
        while q:
            x,y = q.popleft()
            nx = x + dx[k][0]
            ny = y + dx[k][1]
            if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == 'O':
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    flag = max(flag,visited[nx][ny])
    return flag

def x_check(board, dx, i, j):
    flag = 0
    q = deque()
    for k in range(4):
        visited = [[0] * 3 for _ in range(3)]
        q.append((i,j))
        visited[i][j] = 1
        while q:
            x,y = q.popleft()
            nx = x + dx[k][0]
            ny = y + dx[k][1]
            if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == 'X':
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    flag = max(flag,visited[nx][ny])
    return flag

def check(board): # 게임이 끝났어야 하는지 구조를 파악
    dx = [[1,0],[0,1],[1,1],[1,-1]]
    o_flag, x_flag, flag = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_flag = max(o_flag, o_check(board,dx,i,j))
            
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x_flag = max(x_flag, x_check(board, dx, i, j))

    return o_flag, x_flag
                
def solution(board):
    answer = -1
    o_cnt = 0
    x_cnt = 0
    o_flag, x_flag = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_cnt += 1
            elif board[i][j] == 'X':
                x_cnt += 1
    if o_cnt < 3 and x_cnt < 3: # 둘다 3개보다는 작을 때
        if 0 <= o_cnt -  x_cnt <= 1: # 둘의 차이가 1보다 작거나 같을 때만 합격이고 
            return 1
        return 0 # 나머지는 나오면 안 되는 상황이니 0을 리턴
    else: # 3개인 바둑돌이 있다는 거니 구조 파악
        o_flag, x_flag = check(board)
        print(o_flag, x_flag, o_cnt, x_cnt)
        if o_flag == 3: # 선공인 o가 3
            if x_flag == 3:
                return 0
            if o_cnt - x_cnt == 1:
                return 1
            return 0
        elif x_flag == 3: # 후공인 x가 3
            if x_cnt - o_cnt == 0: 
                return 1
            return 0
        # 둘 다 3이 아니었다는 의미니
        if 0 <= o_cnt -  x_cnt <= 1: # 둘의 차이가 1보다 작거나 같을 때만 합격이고 
            return 1
        return 0 # 나머지는 나오면 안 되는 상황이니 0을 리턴
    return answer