from itertools import combinations

# 장애물들을 좌표들 중에서 3개를조합하여 놓고 
# 학생기준으로 선생을 만나기전에 장애물을 상하좌우 방향으로 먼저 마주친다면 ok
# 그렇지 않다면 No를 출력

n = int(input())
data = [list(input().split()) for _ in range(n)]
void = []
stu = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            void.append((i,j))
        if data[i][j] == 'S':
            stu.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(num,student):
    x = student[0]
    y = student[1]
    flag = 0
    t_flag = 0
    while True:
        if x+1 < n: # 정진을 한다 빈 공간이어도 정진 장애물을 먼저 마주쳤다면 yes
            if data[x+1][y] == 'T':
                flag = 1
                break
            if (x+1,y) in num:
                break      
            x += 1
        else:
            break
    if flag == 1:
        return flag     
    x = student[0]
    while True:
        if 0 <= x - 1: # 정진을 한다 빈 공간이어도 정진 장애물을 먼저 마주쳤다면 yes
            if data[x-1][y] == 'T':
                flag = 1
                break
            if (x-1,y) in num:
                break      
            x -= 1
        else:
            break
    if flag == 1:
        return flag
    x = student[0]
    while True:
        if 0 <= y - 1: # 정진을 한다 빈 공간이어도 정진 장애물을 먼저 마주쳤다면 yes
            if data[x][y-1] == 'T':
                flag = 1
                break
            if (x,y-1) in num:
                break      
            y -= 1
        else:
            break
    if flag == 1:
        return flag
    y = student[1]
    while True:
        if y+1 < n: # 정진을 한다 빈 공간이어도 정진 장애물을 먼저 마주쳤다면 yes
            if data[x][y+1] == 'T':
                flag = 1
                break
            if (x,y+1) in num:
                break      
            y += 1
        else:
            break
    return flag

final_flag = 0
for num in combinations(void,3):
    flag = 0
    for student in stu:
        if check(num,student) == 1:
            flag = 1
            break
    if flag == 0:
        print("YES")
        final_flag = 1
        break
if final_flag == 0:
    print("NO")