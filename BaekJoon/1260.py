from collections import deque

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,v = map(int,input().split())

data = [[]  for i in range(n+1)]

d_visited = [0] *(n+1)
b_visited = [0] *(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)


for i in range(n+1):
    data[i].sort()

def dfs(start,data,d_visited):
    print(start,end=' ')
    d_visited[start] = 1
    for i in data[start]:
        if d_visited[i] == 0:
            dfs(i,data,d_visited)

def bfs(start,data,v_visited):
    queue = deque()
    queue.append(start)
    print(start,end=' ')
    b_visited[start] = 1
    while queue:
        x = queue.popleft()
        for i in data[x]:
            if b_visited[i] == 0:
                queue.append(i)
                b_visited[i] = 1
                print(i,end=' ')

dfs(v,data,d_visited)
print()
bfs(v,data,b_visited)

