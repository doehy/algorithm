from collections import deque
import copy
r,c = map(int,input().split())
data = [list(input()) for _ in range(r)]
a = copy.deepcopy(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_x = 0
min_x = float("inf")
max_y = 0
min_y = float("inf")

def bfs(x,y):
    count = 0
    global max_x
    global max_y
    global min_x
    global min_y
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or data[nx][ny] == '.':
            count += 1
        if count == 3:
            a[x][y] = '.'
            break
    if count < 3:
        max_x = max(max_x,x)
        min_x = min(min_x,x)
        max_y = max(max_y,y)
        min_y = min(min_y,y)
        
for i in range(r):
    for j in range(c):
        if data[i][j] == 'X':
            bfs(i,j)


for i in range(min_x,max_x+1):
    for j in range(min_y,max_y+1):
        print(a[i][j],end='')
    print()