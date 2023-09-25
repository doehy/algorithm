import heapq,sys
input = sys.stdin.readline
n = int(input().rstrip())

data = []

sr = []
for i in range(n):
    num, start, end = map(int,input().split())
    sr.append((start,end))

sr = sorted(sr, key=lambda x:x[1])
sr = sorted(sr, key=lambda x:x[0])

i = 0
for start,end in sr:
    if i == 0:
        heapq.heappush(data, end)
        i = 1
        continue
    if start < data[0]:
        heapq.heappush(data,end)
    else:
        heapq.heappop(data)
        heapq.heappush(data,end)

print(len(data))

# 시작 시간을 기준으로 나열한다. 끝나는 시간을 기준으로 
# 2 14    7,13    6, 20    6  27    12,18    

# 처음에는 일단 강의실을 개설하고 끝난 강의가 존재하지 않는다면 계쏙 강의실을 개설한다.
# 힙에 들어가는 구조는 끝나는 시간을 기준으로 들어간다.최소힙 구조로 들어간다. 바로 꺼냈을 때 내가 더 작다면 하나 더 개설 그렇지 않다면 
# 그냥 count 하나 씩 증가시키면 된다. 