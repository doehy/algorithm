import sys,heapq
input = sys.stdin.readline
n,m = map(int,input().split())
see = list(map(int,input().split()))
data = [[] for i in range(n)]

for i in range(m):
    a,b,t = map(int,input().split())
    data[a].append((b,t))
    data[b].append((a,t))

distance = [float("inf")] * (n)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if (node != n-1 and see[node] == 1) or distance[node] < dist:
            continue
        for next in data[node]:
            if next[0] != n-1 and see[next[0]] == 1:
                continue
            cost = next[1] + distance[node]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

dijkstra(0)

if distance[n-1] == float("inf"):
    print(-1)
else:
    print(distance[n-1])