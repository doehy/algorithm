n,m = map(int,input().split())
r,c,d = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check(x,y,d):
    result = 1
    temp = 0
    data[x][y] = 2
    while True : # 4방향이 다 청소되있거나 벽이면서 뒤로도 후진할 수 없는 경우에 탈출인데 흠.... 그냥 일다 true라고하자
        if d == 0:
            d = 3 # 서쪽 방향을 바라보게 하고
            if data[x+dx[d]][y+dy[d]] == 0: #청소하지 않는 공간일 때만 청소한다는 뜻이다.
                x = x + dx[d]
                y = y + dy[d]
                result += 1
                temp = 0
                data[x][y] = 2
            else:
                temp += 1
                if temp == 4:
                    if data[x+dx[1]][y+dy[1]] == 1:
                        break
                    else:
                        x = x + dx[1]
                        y = y + dy[1]
                        temp = 0
        elif d == 1:
            d = 0
            if data[x+dx[d]][y+dy[d]] == 0:
                x = x + dx[d]
                y = y + dy[d]
                result += 1
                temp = 0
                data[x][y] = 2
            else:
                temp += 1
                if temp == 4:
                    if data[x+dx[2]][y+dy[2]] == 1:
                        break
                    else:
                        x = x + dx[2]
                        y = y + dy[2]
                        temp = 0
        elif d == 2:
            d = 1
            if data[x+dx[d]][y+dy[d]] == 0:
                x = x + dx[d]
                y = y + dy[d]
                temp = 0
                result += 1
                data[x][y] = 2
            else:
                temp += 1
                if temp == 4:
                    if data[x+dx[3]][y+dy[3]] == 1:
                        break
                    else:
                        x = x + dx[3]
                        y = y + dy[3]
                        temp = 0
        else:
            d = 2
            if data[x+dx[d]][y+dy[d]] == 0:
                x = x + dx[d]
                y = y + dy[d]
                temp = 0
                result += 1
                data[x][y] = 2
            else:
                temp += 1
                if temp == 4:
                    if data[x+dx[0]][y+dy[0]] == 1:
                        break
                    else:
                        x = x + dx[0]
                        y = y + dy[0]
                        temp = 0
    return result
print(check(r,c,d))
