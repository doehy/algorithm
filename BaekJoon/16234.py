from collections import deque

n,l,r = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

day = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[-1]*n for _ in range(n)]

cnt = 0

queue = deque()
for q in range(n):
    for p in range(n): # 그래프 전체를 돌고 있는 중이다.
        for j in range(4):
            nx = q + dx[j]
            ny = p + dy[j]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and l<=array[q][p]-array[nx][ny]<=r: # 그래프안에 있으면서 방문한적 없고 수 사이일 때만
                queue.append(array[nx][ny]) 
                visited[nx][ny] = 0
                cnt += 1

    if cnt == 0:
        break


queue.append(x,y)
visit = [[-1]*n for i in range(n)]
while queue:
    x,y = queue.popleft()
    sum = 0 # 처음 sum은 0으로 초기화
    cnt = 0 #개수를 세줄 변수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==-1:
            visit[nx][ny] = 0
            if l<=abs(array[nx][ny] - array[x][y])<=r:
                cnt+=1
                

