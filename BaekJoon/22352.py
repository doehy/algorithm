from collections import deque

n,m = map(int,input().split())
before = [list(map(int,input().split())) for i in range(n)]
after = [list(map(int,input().split())) for i in range(n)]
visited = [[0] * m for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(i,j,afterNumber,beforeNumber):
    global answer
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    if afterNumber != beforeNumber: # 값이 달라졌어 그러면 값을 하나 증가시켜
        answer += 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and before[x][y] == before[nx][ny]: # 애초부터 이 값인 것만 들여보낸다.
                if after[nx][ny] == afterNumber and visited[nx][ny] == 0:
                    visited[nx][ny] = 1 # 방문처리를 해준다.
                    q.append((nx,ny)) # 큐에 nx,ny를 추가한다.    
                if  after[x][y] != after[nx][ny]:
                    answer += 100 # 끝내라는 의미이다 더 이상 볼게 없다.
                    return

answer = 0
flag = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0: # 그냥 방문한 적 없으면 다 확인해야한다.
            check(i,j,after[i][j],before[i][j]) 
        if answer > 1: # 1 이상이면 더 이상 볼 것도 없으니까
            flag = 1
            break
    if flag == 1:
        break

if answer > 1:
    print("NO")
else:
    print("YES")  