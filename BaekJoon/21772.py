from collections import deque
import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total = 0
visited = [[0] * c for _ in range(r)]
def check(i,j,time,num):
    global total
    if time == t:
        total = max(total,num)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
            if graph[nx][ny] == 'S' and not visited[nx][ny]:
                visited[nx][ny] = 1
                check(nx,ny,time+1,num+1)
                visited[nx][ny] = 0 
            else:
                check(nx,ny,time+1,num)    

def solve():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'G':
                check(i,j,0,0)
                return
solve()
print(total)