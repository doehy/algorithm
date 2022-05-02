from collections import deque

def paint(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))
    cnt = 1
    graph[x][y] = 0
    while queue:
        a,b = queue.popleft()
        for k in range(4):
            na = a + da[k]
            nb = b + db[k]
            if 0 <= na < n and 0 <= nb < m and graph[na][nb] == 1:    
                graph[na][nb] = 0
                queue.append((na,nb))
                cnt +=1

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

data = [] #그림의 개수를 모아놓을 곳이다.
picture = 0

da = [-1,1,0,0]
db = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint(i,j) 
            picture += 1 # 그림의 개수로 출력될 것
            data.append(cnt)
            cnt = 0

print(picture)
print(max(data) if data else 0)

