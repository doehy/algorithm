import heapq

n = int(input())
data = []
for i in range(n):
    temp = list(map(int,input().split()))
    if len(temp) ==  1 and len(data) == 0:
        print(-1)
        continue
    if len(temp) == 1 and len(data) > 0:
        print(-heapq.heappop(data))
    for i in range(1,len(temp)):
        heapq.heappush(data, -temp[i])
    