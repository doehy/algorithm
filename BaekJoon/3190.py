import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for i in range(n)]

for i in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

l = int(input())

visited = [[0] *n for i in range(n)]
q = deque()
rotate = dict()
# 여기서부터 게임시작
for i in range(l):
    x,c = input().rstrip().split()
    rotate[int(x)] = c

answer = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
r,c = 0,0
q.append((r,c))
visited[r][c] = 1
flag = 0
while True:
    answer += 1
    nr = r + dx[flag]
    nc = c + dy[flag]
    if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
        q.append((nr,nc)) # 뱀 길이 늘려주고
        visited[nr][nc] = 1 # 뱀 길이 늘려주고
        if graph[nr][nc] == 1:
            graph[nr][nc] = 0      
        else:
            x,y = q.popleft()
            visited[x][y] = 0
        r,c = nr,nc
        if answer not in rotate:
            continue
        else:
            if rotate[answer] == "L":
                flag = (flag - 1) % 4
            else:
                flag = (flag + 1) % 4
    else:
        break

print(answer)