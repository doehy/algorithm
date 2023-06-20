import sys,heapq
input = sys.stdin.readline
n,m,r = map(int,input().split())
item = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))
answer = 0
def dijkstra(s):
    itemNum = 0
    distance = [float("inf")] * (n+1)
    q = []
    distance[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next in graph[cur]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    for i in range(1,len(distance)):
        if m >= distance[i]:
            itemNum += item[i]
    return itemNum

for i in range(1,n+1): #1,2,3,4,5
    answer = max(answer,dijkstra(i))

print(answer)