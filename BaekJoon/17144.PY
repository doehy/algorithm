import copy
r,c,t = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(r)]
ch_data = copy.deepcopy(data)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(i,j,ch_data,data):
    num = 0
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < r and 0 <= nj < c and data[ni][nj] != -1:
            ch_data[ni][nj] += data[i][j] // 5
            num += 1
    ch_data[i][j] -= data[i][j] // 5 * num

def u_clear(x,r,c):
    for i in range(x-1,-1,-1):
        if i == x-1:
            ch_data[i][0] = 0
        else:
            ch_data[i+1][0] = ch_data[i][0]
    for i in range(1,c):
        ch_data[0][i-1] = ch_data[0][i]
    for i in range(1,x+1):
        ch_data[i-1][c-1] = ch_data[i][c-1]
    for i in range(c-2,0,-1):
        ch_data[x][i+1] = ch_data[x][i]
    ch_data[x][1] = 0     
     
def d_clear(x,r,c):
    for i in range(x+1,r):
        if i == x+1:
            ch_data[i][0] = 0
        else:
            ch_data[i-1][0] = ch_data[i][0]
    for i in range(1,c):
        ch_data[r-1][i-1] = ch_data[r-1][i]
    for i in range(r-2,x-1,-1):
        ch_data[i+1][c-1] = ch_data[i][c-1]
    for i in range(c-2,0,-1):
        ch_data[x][i+1] = ch_data[x][i]
    ch_data[x][1]=0
# 청소기 위치 구하는 거다.
for i in range(r):
    if data[i][0] == -1:
        u_x = i
        break 
d_x = u_x + 1

while t > 0:
    for i in range(r):
        for j in range(c):
            if data[i][j] >= 5:
                check(i,j,ch_data,data)
    u_clear(u_x,r,c)
    d_clear(d_x,r,c)
    
    data = copy.deepcopy(ch_data)
    t -= 1

result = 0
for i in range(r):
    for j in range(c):
        if data[i][j] != -1:
            result += data[i][j]
print(result)
