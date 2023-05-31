import heapq,sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    x,y = map(int,input().split())
    data.append([x,y])
data.sort()
seat = [[float("inf"),-1]]
empty = []
answer = []

for s,e in data:
    if seat[0][0] > s:
        if len(seat) - 1 < len(answer):
            if len(empty) < 1:
                answer[len(seat) - 1] += 1
                heapq.heappush(seat,[e,len(seat) - 1])
            else:
                answer[empty[0]] += 1
                heapq.heappush(seat,[e,empty[0]])
                heapq.heappop(empty)
        else:
            answer.append(1)
            heapq.heappush(seat,[e,len(seat) - 1])
    else:
        while True:    
            if len(seat) > 0 and seat[0][0] < s:
                end_time, idx = heapq.heappop(seat)
                heapq.heappush(empty, idx)
            else: 
                heapq.heappush(seat, [e, empty[0]]) 
                answer[empty[0]] += 1
                heapq.heappop(empty)
                break
print(len(answer))
print(*answer)
