n = int(input())

text = input()

dif = 3

data = [[0,0]]
x = 0
y = 0
dx = [0,-1,0,1]
dy = [-1,0,1,0]

max_x = 0
max_y = 0
min_x = 0
min_y = 0

for i in range(len(text)):
    temp = text[i]
    if temp == 'R':
        dif += 1
    elif temp == 'L':
        dif -= 1
    else:
        if dif % 4 == 1:
           x = x + dx[1]
           y = y + dy[1]
           data.append([x,y])
           max_x = max(max_x,x)
           max_y = max(max_y,y)
           min_x = min(min_x,x)
           min_y = min(min_y,y)
        elif dif % 4 == 2:
            x = x + dx[2]
            y = y + dy[2]
            data.append([x,y])
            max_x = max(max_x,x)
            max_y = max(max_y,y)
            min_x = min(min_x,x)
            min_y = min(min_y,y)
        elif dif % 4 == 3:
            x = x + dx[3]
            y = y + dy[3]
            data.append([x,y])
            max_x = max(max_x,x)
            max_y = max(max_y,y)
            min_x = min(min_x,x)
            min_y = min(min_y,y)
        else:
            x = x + dx[0]
            y = y + dy[0]
            data.append([x,y])
            max_x = max(max_x,x)
            max_y = max(max_y,y)
            min_x = min(min_x,x)
            min_y = min(min_y,y)

x = max_x - min_x
y = max_y - min_y

jido = [[False] * (y+1) for i in range(x+1)]

if min_x < 0:
    for i in range(len(data)):
        data[i][0] += abs(min_x)

if min_y < 0:
    for i in range(len(data)):
        data[i][1] += abs(min_y)

#이제 데이터도 정리 다했고 지도도 다 만들어놨어

for i in range(x+1):
    for j in range(y+1):
        if [i,j] not in data:
            jido[i][j] = '#'
        else:
            jido[i][j] = '.'

for i in range(x+1):
    print(''.join(jido[i][:]))
