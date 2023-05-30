import sys, heapq
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    s,e = map(int,input().split())
    data.append([s,e])
data.sort()
answer = 0
seat = [float("inf")]
for s,e in data:
    if seat[0] > s:
        heapq.heappush(seat,e)
        answer += 1
    elif seat[0] <= s: 
        heapq.heappop(seat)
        heapq.heappush(seat,e) 

print(len(seat) - 1)

