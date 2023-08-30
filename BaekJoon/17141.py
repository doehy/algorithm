from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
for _ in range(n):
	data.append(list(map(int,input().split())))
possible = []
wall = 0
for i in range(n):
	for j in range(n):
		if data[i][j] == 2:
			possible.append([i,j])
		elif data[i][j] == 1:
			wall += 1
result = n*n - wall
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = float("inf")
def check(lis):
	visited = [[-1] * n for _ in range(n)]
	count = 0
	q = deque()
	for x,y in lis:
		q.append([x,y])
		visited[x][y] = 0
		count += 1
	while q:
		x,y = q.popleft()
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and data[nx][ny] != 1:
				q.append([nx,ny])
				visited[nx][ny] = visited[x][y] + 1
				count += 1
	if count == result:
		return max(map(max,visited))
	else:
		return float("inf")

for lis in combinations(possible,m):
	answer = min(answer,check(lis))

if answer == float("inf"):
	print(-1)
else:
	print(answer)
