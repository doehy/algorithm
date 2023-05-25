import sys
input = sys.stdin.readline
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def pin_check():
    global count
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'o':
                count += 1

def move():
    global moving, cnt
    moving = max(moving, cnt) 
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'o':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < len(data) and 0 <= ny < len(data[i]) and data[nx][ny] == 'o':
                        nnx = nx + dx[k]
                        nny = ny + dy[k]
                        if 0 <= nnx < len(data) and 0 <= nny < len(data[i]) and data[nnx][nny] == '.':
                            data[i][j] = '.'
                            data[nx][ny] = '.'
                            data[nnx][nny] = 'o'
                            cnt += 1
                            move()
                            data[i][j] = 'o'
                            data[nx][ny] = 'o'
                            data[nnx][nny] = '.'
                            cnt -= 1

for i in range(n):
    moving = 0
    cnt = 0
    count = 0
    data = [list(input().rstrip()) for i in range(5)]
    if i != n - 1:
        input()
    pin_check()
    move()
    print(count - moving, moving)
