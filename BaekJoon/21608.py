n = int(input())
table = [[False] * n for _ in range(n)]
data = [list(map(int,input().split())) for _ in range(n*n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
def final(temp,side_data,person):
    flag = 0
    for i in range(n):
        for j in range(n):
            if side_data[i][j] == max(map(max,side_data)) and temp[i][j] == max(map(max,temp)):
                table[i][j] = person[0] 
                flag = 1
                break
        if flag == 1:
            break
    
def side(temp,person):
    side_data = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if temp[i][j] == max(map(max,temp)):
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<= ni < n and 0<= nj < n and table[ni][nj] == False:
                        side_data[i][j] += 1
    
    final(temp,side_data,person)
def sit(person):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == False: # 아무도 앉지 않은 자리라면
                temp[i][j] = 1
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<= ni < n and 0<= nj < n and table[ni][nj] in person: # 범위 안에 있고 좋아하는 사람까지 있는지
                        temp[i][j] += 1
    
    side(temp,person)

def sum(person):
    global result
    temp = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] == person[0]:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0<= nj < n and table[ni][nj] in person:
                        temp += 1
    if temp == 0:
        pass
    else:
        result += 10 ** (temp-1)
for person in data:
    sit(person)

for person in data:
    sum(person)

print(result)