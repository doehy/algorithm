from collections import deque

n,m = map(int,input().split())

start = []
end = []
for i in range(n+m):
    x,y = map(int,input().split())
    start.append(x)
    end.append(y)

dx = [1,2,3,4,5,6]

def bfs(s,visited):
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        x = q.popleft()
        for i in range(6):
            nx = x + dx[i] 
            if visited[nx] == -1:# 방문한 적이 한 번도 없으면서
                visited[nx] = visited[x] + 1
                if nx >= 100:
                    return visited[nx]
                if nx in start:
                    number = end[start.index(nx)]
                    if visited[number] == -1: # 8% -> 22%
                        visited[number] = visited[x] + 1
                        q.append(number)
                else:
                    q.append(nx)

visited = [-1] * 108
print(bfs(1,visited))