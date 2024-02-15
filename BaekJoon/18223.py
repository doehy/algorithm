from heapq import heappush, heappop
import sys
input = sys.stdin.readline
v,e,p = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [float("inf") for _ in range(v+1)]
pDistance = [float("inf") for _ in range(v+1)]

def dijkstra(start):
    q = []
    heappush(q, [0, start])
    distance[start] = 0
    while q:
        cost, cur = heappop(q) 
        for next,c in graph[cur]:
            totalCost = cost + c
            if distance[next] > totalCost:
                distance[next] = totalCost
                heappush(q, [totalCost, next])

def pDijkstra(start):
    q = []
    heappush(q, [0, start])
    pDistance[start] = 0
    while q:
        cost, cur = heappop(q) 
        for next,c in graph[cur]:
            totalCost = cost + c
            if pDistance[next] > totalCost:
                pDistance[next] = totalCost
                heappush(q, [totalCost, next])
dijkstra(1)
pDijkstra(p)
if distance[v] == distance[p] + pDistance[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
