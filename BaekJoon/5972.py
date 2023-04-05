import sys, heapq
input = sys.stdin.readline

n, m = map(int,input().split())
INF = float("inf")
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c)) # 양방향이라고 해서 일단 양방향으로 받음 근데 똑같은 길을 쓰고 있는데 그냥 한 방향으로만 받으면 되는 것 아닌가

def dijkstra(s):
    q = []
    distance[s] = 0 # 자기자신에 대해서는 0이어야지
    heapq.heappush(q,(0,s)) # 거리 위치로 heapq에 들어간다.
    while q:
        dist, cur = heapq.heappop(q) #
        if distance[cur] < dist: # 새로 거리를 꺼냈는데 이미 있던 것보다 컸으면 다음 껄로 넘어간다.
            continue # 그게 아니라면
        for next in graph[cur]: # 이웃된 노드 중에서
            cost = dist + next[1] # 원래 연결돼 있던 거리와 연결된 거리? 암튼
            if cost < distance[next[0]]: # 원래 연결돼 있던게 최소가 아니었다면
                distance[next[0]] = cost # 새롭게 거리를 갱신해주고
                heapq.heappush(q,(cost, next[0]))
    return distance[n]

print(dijkstra(1))
