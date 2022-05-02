from collections import deque

def bfs(start):
    cnt = 0
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

n,m = map(int,input().split())

graph=[[] for _ in range(n+1)]

computer=[]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

max_cnt = 0

for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt        
    computer.append([i,cnt])

for i,cnt in computer:
    if cnt == max_cnt:
        print(i,end=' ')




