from collections import deque

t = int(input())

def bfs(graph):
    queue = deque()
    

    

for _ in range(t):
    n = int(input())
    h_x,h_y = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    festival_x,festival_y = map(int,input().split())
    graph.append(festival_x,festival_y)
    
