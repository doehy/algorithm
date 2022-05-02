from collections import deque
import sys

dx = [-1,1,2]
def bfs(source):
    queue = deque()
    queue.append(source)
    data[source] = 0
    while queue:
        x = queue.popleft()
        for i in dx:        
            nx = x * 2 if i == 2 else x + i
            if 0 <= nx <= 100000 and data[nx] == -1:
                queue.append(nx)
                data[nx] = data[x] + 1
            if nx == m:
                return data[nx]

data = [-1 for _ in range(100001)]
n,m = map(int,sys.stdin.readline().split())
print(bfs(n))