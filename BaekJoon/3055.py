from collections import deque
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
data = [list(input().rstrip()) for i in range(r)]
startR = startC = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(wq, i,j):
    answer = 0
    q = deque()
    q.append((i,j))
    while True:
        answer += 1
        for _ in range(len(wq)):
            x,y = wq.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != 'D' and data[nx][ny] != 'X' and data[nx][ny] != '*': # 수달집, 벽돌
                    wq.append((nx,ny))
                    data[nx][ny] = '*'       
        for _ in range(len(q)):
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != '*' and data[nx][ny] != 'X' and data[nx][ny] != 'S': #방문한 적 없고 돌덩이가 아니라면
                    if data[nx][ny] == 'D':
                        return answer
                    data[nx][ny] = 'S'
                    q.append((nx,ny)) 
        if len(q) == 0:
            return 0
# 고슴도치가 움직인 칸은 1로 해놔야 한다.
wq = deque() 
for i in range(r):
    for j in range(c):
        if data[i][j] == '*':
            wq.append((i,j))
        if data[i][j] == 'S':
            startR, startC = i,j
answer = check(wq,startR, startC)

if answer:
    print(answer)
else:
    print("KAKTUS")
