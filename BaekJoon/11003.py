from collections import deque
import sys
input = sys.stdin.readline
n,l = map(int,input().split())
data = list(map(int,input().split()))
## 최솟값을 구할 곳
temp = deque([])

for i in range(n):
    ## 슬라이딩
    if temp and temp[0][0] <= i-l:
        temp.popleft()

    ## 들어올 원소가 기존의 원소보다 작으면 기존원소 삭제
    while len(temp) >= 1 and data[i] < temp[-1][1]:
        temp.pop()
    
    temp.append((i,data[i]))

    print(temp[0][1], end = " ")