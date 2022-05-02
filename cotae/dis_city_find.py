from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)] # 인덱스가 4까지 생길 것이다.

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1) #인덱스 4까지 -1로 초기화 될 것이다.
distance[x] = 0


queue = deque([x])

while queue:
    number = queue.popleft()
    for i in graph[number]:
        if distance[i] == -1:
        distance[i] = distance[number] + 1
        queue.append(i)


check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
