import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
distance = [float("inf")] * (n +1)
data = [[] for _ in range(n+1)]
for i in range(m):
    s,e,d = map(int,input().split())
    data[s].append((e,d))

start,end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0 # 시작노드 -> 시작노드 거리 기록
    while q:
        dist, node = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드를 탐색
        for next in data[node]:
            cost = distance[node] + next[1] # 시작 -> node 거리 + node-> node의 인접노드 거리
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

dijkstra(start)
print(distance[end])
 