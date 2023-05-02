n,m,r,c,k = map(int,input().split())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

command = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0]
# 밑면, 뒷면,윗면,앞면,왼쪽면,오른쪽면
def turn(moving):
    if moving == 1: # 동쪽 # 0-> 4, 1-> 1, 2-> 5, 3-> 3, 4-> 2, 5-> 0
       dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]              
    elif moving == 2: # 서쪽 # 0->5, 1-> 1, 2-> 4, 3-> 3, 4-> 0, 5-> 2
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]
    elif moving == 3: # 북쪽 # 0->3, 1->0, 2->1 , 3->2, 4->4, 5->5 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]
    else: # 남쪽 # 0->1, 1->2, 2->3, 3->0, 4->4, 5->5
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]

for moving in command:
    nr = r + dx[moving-1]
    nc = c + dy[moving-1]
    if 0 <= nr < n and 0 <= nc < m:
        turn(moving)
        print(dice[2])
        if data[nr][nc] == 0:
            data[nr][nc] = dice[0]
        else:
            dice[0] = data[nr][nc]
            data[nr][nc] = 0
    else:
        nr -= dx[moving-1]
        nc -= dy[moving-1]
        continue
    r,c = nr,nc