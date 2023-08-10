from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
visited = [[float("inf"),0] for _ in range(100001)]
def bfs(start, end):
    q = deque()
    q.append([start,0])
    while q:
        x, count = q.popleft()
        nx = x -1
        if 0 <= nx <= 100000:
            if visited[nx][0] > count + 1:
                q.append([nx, count + 1]) 
                visited[nx][0] = count + 1
                visited[nx][1] = 1
            elif visited[nx][0] == count + 1:
                q.append([nx, count + 1])
                visited[nx][1] += 1
                
        nx = x + 1
        if 0 <= nx <= 100000:
            if visited[nx][0] > count + 1:
                q.append([nx, count + 1]) 
                visited[nx][0] = count + 1
                visited[nx][1] = 1
            elif visited[nx][0] == count + 1:
                q.append([nx, count + 1])
                visited[nx][1] += 1
    
        nx = x * 2
        if 0 <= nx <= 100000:
            if visited[nx][0] > count + 1:
                q.append([nx, count + 1]) 
                visited[nx][0] = count + 1
                visited[nx][1] = 1
            elif visited[nx][0] == count + 1:
                q.append([nx, count + 1])
                visited[nx][1] += 1

if n == k:
    print(0)
    print(1)
else:
    bfs(n,k)
    print(visited[k][0])
    print(visited[k][1])
