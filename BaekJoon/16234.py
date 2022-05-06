from collections import deque

n,l,r = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

day = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
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
                    

