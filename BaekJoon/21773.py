import sys,heapq
input = sys.stdin.readline
t,n = map(int,input().split())
data = []
for _ in range(n):
    a,b,c = map(int,input().split())
    heapq.heappush(data,[-c,a,b])

for _ in range(t):
    cc, ca, cb = heapq.heappop(data)
    cc = -cc # 생각하기 쉽게 잠시 양수로
    print(ca)
    if cb -1 > 0:
        heapq.heappush(data,[-cc+1, ca , cb - 1]) 