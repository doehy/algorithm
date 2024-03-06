import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
x = int(input())

def check(start):
    result = 0
    q = deque()
    q.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                result += 1
                q.append(next)
    return result            

print(check(x))