from collections import deque

t = int(input())

def bfs():
    queue = deque()
    queue.append(start)
    visited = [False] * n
    while queue:
        x,y = queue.popleft()
        if abs(end[0]-x) + abs(end[1]-y) <= 1000:
            return True
        for i in range(n):
            if visited[i] == False:
                nx,ny = data[i]
                if abs(nx-x) + abs(ny-y) <=1000:
                    visited[i] = True
                    queue.append([nx,ny])
    return False

for _ in range(t):
    n = int(input())
    start = list(map(int,input().split()))
    data = [list(map(int,input().split())) for _ in range(n)]
    end = list(map(int,input().split()))
    result = bfs()
    if result:
        print('happy')
    else:
        print('sad')