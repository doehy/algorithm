import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[0] * a for _ in range(b)]
robot = []
for _ in range(n):
    x,y,d = input().split()
    x,y = int(x), int(y)
    graph[y - 1][x - 1] = 1
    if d == "N":
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    robot.append([y - 1 , x - 1 , d]) # 로봇들을 기억해놓는다. 여기서

commands = []

for _ in range(m):
    num, command, frequency = input().split()
    commands.append([int(num), command, int(frequency)])

# 상N, 우E, 하S, 좌W
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(lis):
    if lis[1] == "R":
        robot[lis[0] - 1][2] = (robot[lis[0] - 1][2] + 1 * lis[2]) % 4
    elif lis[1] == 'L':
        robot[lis[0] - 1][2] = (robot[lis[0] - 1][2] -1 * lis[2]) % 4
    else:
        r , c = robot[lis[0] - 1][0], robot[lis[0] - 1][1]
        nr , nc = r , c
        for i in range(lis[2]):
            nr = nr + dx[robot[lis[0] - 1][2]]
            nc = nc + dy[robot[lis[0] - 1][2]]
            if 0 <= nr < b and 0 <= nc < a:
                if graph[nr][nc] == 1:
                    for i in range(len(robot)):
                        if nr == robot[i][0] and nc == robot[i][1]:
                            collision = i + 1
                    print("Robot " + str(lis[0]) + " crashes into robot " + str(collision))
                    return 1
            else:
                print("Robot " + str(lis[0]) + " crashes into the wall")
                return 1
        graph[r][c] = 0 
        graph[nr][nc] = 1
        robot[lis[0] - 1][0], robot[lis[0] - 1][1] = nr, nc # 새로운 좌표를 넣어준다.

flag = 0
for lis in commands:
    if check(lis):
        flag = 1
        break

if flag == 0:
    print("OK")