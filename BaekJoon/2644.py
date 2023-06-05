from collections import deque
n = int(input())
x,y = map(int,input().split())
m = int(input())
data = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

visited = [float("inf") for _ in range(n+1)]

def check(s,e,visited):
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        start = q.popleft()
        for node in data[start]:
            if visited[node] == float("inf"):
                visited[node] = visited[start] + 1
                q.append(node)
    return visited[e]
# 방문 처리를 안 해줄경우 무한 반복을 한다. 
# 여기서 의문점이 드는 부분 연결되있는 부분이 앞이 아니라 뒤에 있었다면? 역시 틀림 count가 계속 더해지기 때문에
# 트리 구조이기에 min 처리를 할 필요가 있나? 갔던 곳은 또 가지 않는데 min을 빼보자
if check(x,y,visited) == float("inf"):
    print(-1)
else:
    print(visited[y])


