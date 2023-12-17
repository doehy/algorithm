import sys,heapq
input = sys.stdin.readline

n,h,t = map(int,input().split())
height = [-int(input()) for _ in range(n)]
heapq.heapify(height)
cnt = 0

for i in range(t):
    if -height[0] == 1 or -height[0] < h:
        break
    else:
        heapq.heapreplace(height,(-height[0] // 2) * -1)
        cnt += 1

if -height[0] >= h:
    print("NO",-height[0],sep='\n')
else:
    print("YES",cnt,sep='\n')

