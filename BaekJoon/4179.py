from collections import deque
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
graph = []
fires = deque()
jihoon = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
flag = 0
for i in range(r):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'J':
            jihoon.append([i,j])
        if temp[j] == 'F':
            fires.append([i,j])
    graph.append(temp)
    
def movePerson():
    global count,flag
    if len(jihoon) == 0:
        flag = 1
        return
    count += 1
    for _ in range(len(jihoon)):
        x,y = jihoon.popleft()
        if graph[x][y] != 'J':
            continue
        graph[x][y] = 'VJ'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx == r or ny < 0 or ny == c: #밖으로 탈출한다면
                flag = 2
                return
            else: #범위 안에 있고
                if graph[nx][ny] == '.':
                    jihoon.append([nx,ny]) 
                    graph[nx][ny] = 'J'

def moveFire():
    for _ in range(len(fires)):
        x,y = fires.popleft()
        graph[x][y] = 'VF'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 'VF' and graph[nx][ny] != '#': 
                fires.append([nx,ny])
                graph[nx][ny] = 'F'     


def solve():
    movePerson()
    if flag == 1 or flag == 2:
        return # 밑으로 내려갈 필요가 없으니
    moveFire()

while True:
    solve()
    if flag == 1:
        print("IMPOSSIBLE")
        break
    elif flag == 2:
        print(count)
        break
