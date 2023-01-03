from collections import deque

n,k = map(int,input().split())

data = [0] * (100001)
visited = [False] * (100001)
dx = [2,1,-1]

def bfs(n,k):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        x = q.popleft()
        for i in range(3):
            if i == 0:
                nx = x * dx[i]
                if 0 <= nx <= 100000 and visited[nx] == True:
                    data[nx] = min(data[x],data[nx])
                if 0 <= nx <= 100000 and visited[nx] == False:
                    data[nx] = data[x]
                    visited[nx] = True
                    q.appendleft(nx)
                
            else:
                nx = x + dx[i]
                if 0 <= nx <= 100000 and visited[nx] == True:
                    data[nx] = min(data[x] + 1,data[nx])
                if 0 <= nx <= 100000 and visited[nx] == False:
                    data[nx] = data[x] + 1
                    visited[nx] = True
                    q.append(nx)
            if nx == k:
                return

bfs(n,k)
print(data[k])