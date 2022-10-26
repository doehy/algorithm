from collections import deque

n,m = map(int,input().split())

data = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

def check(i):
    visited = [0] * (n+1) 
    q = deque([i])
    visited[i] = 1
    while q:
        x = q.popleft()
        for k in data[x]:
            if visited[k] == 0:
                visited[k] = True
                q.append(k)
                visited[k] = visited[x] + 1
    return sum(visited)

min_result = float("INF")

for i in range(1,n+1):
    if min_result > check(i):
        min_result = check(i)
        result = i
print(result)
