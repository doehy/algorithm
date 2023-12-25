from collections import deque
n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
cloud = [[False] * n for _ in range(n)]
q = deque()
q.append((n-2,0))
q.append((n-1,0))
q.append((n-2,1))
q.append((n-1,1))
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
temp_q = deque()
for i in range(m):
    d,s = map(int,input().split())
    while q:
        x,y = q.popleft() 
        x = (n+x+dx[d-1]*s) % n
        y = (n+y+(dy[d-1]*s)) % n
        data[x][y] += 1
        cloud[x][y] = True
        temp_q.append([x,y])
    while temp_q:
        x,y = temp_q.popleft()
        for k in range(1,8,2):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > 0:
                data[x][y] += 1
    for i in range(n):
        for j in range(n):
            if data[i][j] >= 2 and cloud[i][j] == False : #2이 이상이면 원래 구름이 없던 자리이어야 한다.
                data[i][j] -= 2
                q.append((i,j))
            elif cloud[i][j] == True: #구름이 있던자리였다면 구름을 없애준다.
                cloud[i][j] = False
    
result = 0
for i in range(n):
    for j in range(n):
        result += data[i][j]
print(result)