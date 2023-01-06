import sys,heapq
input = sys.stdin.readline
n,m = map(int,input().split())
present = list(map(int,input().split()))
wanted = list(map(int,input().split()))
heap = []
flag = 0

for i in present: 
    heapq.heappush(heap,-i)

for num in wanted:
    maxnum = -heapq.heappop(heap)
    if maxnum > num:
        maxnum -= num
        heapq.heappush(heap,-maxnum)
    elif maxnum == num:
        pass # 
    else:
        print(0)
        flag = 1
        break
    
if flag == 0:
    print(1)