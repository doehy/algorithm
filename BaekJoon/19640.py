from collections import deque
import heapq
n,m,k = map(int,input().split())
data = [deque([]) for i in range(m)]
heap = []

for i in range(n):
    day,fast = map(int,input().split())
    if i < m:
        if i == k:
            heapq.heappush(heap, [-day,-fast,i,"o"])
        else:
            heapq.heappush(heap, [-day,-fast,i,"x"])
    else:
        if i == k:
            data[i%m].append(deque([day,fast] + [i%m,"o"]))
        else:
            data[i%m].append(deque([day,fast] + [i%m,"x"]))

answer = 0

while True:
    day, fast, idx, ox = heapq.heappop(heap)
    if ox == 'o':
        break
    if len(data[idx]) > 0:
        day, fast, idx, ox= data[idx].popleft()
        heapq.heappush(heap, [-day, -fast, idx, ox])
    answer += 1

print(answer)