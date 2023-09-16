# 게임
import sys
from collections import deque
input = sys.stdin.readline
d = int(input())
graph = [[0] * 501 for _ in range(501)]
for _ in range(d):
    x,y,x1,y1 = map(int,input().split())
    if x > x1:
        x,x1 = x1, x
    if y > y1:
        y,y1 = y1,y
    for i in range(x,x1+1):
        for j in range(y, y1+1):
            graph[i][j] = 1
de = int(input())
for _ in range(de):
    x,y,x1,y1 = map(int,input().split())
    if x > x1:
        x,x1 = x1, x
    if y > y1:
        y,y1 = y1,y
    for i in range(x,x1+1):
        for j in range(y, y1+1):
            graph[i][j] = 2

move = [(-1,0), (1,0), (0,1), (0,-1)]
def check(sx, se, visited):
    visited[sx][se] = 0
    q = deque()
    q.append((sx,se))
    while q:
        x,y = q.popleft()
        for moving in move:
            nx = x + moving[0]; ny = y + moving[1]
            if 0 <= nx < 501 and 0 <= ny < 501:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        q.appendleft((nx,ny))
                        visited[nx][ny] = visited[x][y]
                    elif graph[nx][ny] == 1:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
visited = [[-1] * 501 for _ in range(501)]
check(0,0,visited)
print(visited[500][500])
