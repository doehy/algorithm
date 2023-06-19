import heapq
n = int(input())
data = list(map(int,input().split()))
plus = list()
minus = list()
for i in range(len(data)):
    if data[i] > 0:
        heapq.heappush(plus, (i, data[i]))
    else:
        heapq.heappush(minus, (i, data[i]))
answer = 0
plusNum = 0

if n == 1 or len(minus) == 0 or len(plus) == 0:
    print(0)
else:
    while len(minus) > 0 or len(plus) > 0:
        if plusNum <= 0: 
            pIdx, plusNum =  heapq.heappop(plus)
        mIdx, minusNum = heapq.heappop(minus)    
        if -minusNum <= plusNum:
            answer += -minusNum * abs(mIdx - pIdx)
            plusNum += minusNum
            continue
        answer += plusNum * abs(mIdx - pIdx)
        minusNum += plusNum
        while minusNum < 0:  
            pIdx, plusNum = heapq.heappop(plus)
            if -minusNum <= plusNum:
                answer += -minusNum * abs(mIdx - pIdx)
                plusNum += minusNum
                break
            answer += plusNum * abs(mIdx - pIdx)
            minusNum += plusNum
    print(answer)
