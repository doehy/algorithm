from collections import deque
n,m = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int,input())))    

number = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
queue.append((0,0))
data[0][0] = 1
flag = 0

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < m: #그래프 안에 들어갈 수 있다면
            if number == 1 and data[nx][ny] == 1: #벽을 뚫을 수 있는 기회가 1이 남아있고 다음칸이 벽이라면
                for j in range(4): #4방향을 봐본다.
                    px = nx + dx[j]
                    py = ny + dy[j]
                    if 0 <= px < n and 0<= py< m and data[px][py] == 0: #4방향중 한 방향이라도 0이 있으면 가도 된다는 것이다. 그러면 깃발을 올린다.
                        flag = 1
                if flag == 1: #깃발이 올려졌다면 그 해당하는 칸을 큐에 넣고 값 초기화 해주고 벽 뚫을 ㅅ 있는 기회를 한 번 없앤다.
                    queue.append((nx,ny))
                    data[nx][ny] = data[x][y] + 1
                    number -= 1
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))

if data[n-1][m-1] == 0:
    print(-1)
else:
    print(data[n-1][m-1])