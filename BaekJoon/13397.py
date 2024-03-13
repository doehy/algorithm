# 구간 나누기 2
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))

def divide(x):
    cnt = 1 
    maxN = minN = data[0]
    for i in range(1,len(data)):
        maxN = max(maxN, data[i])
        minN = min(minN, data[i])
        if maxN - minN > x:
            cnt += 1
            maxN = data[i]
            minN = data[i]
    return cnt


start, end = 0, max(data)
result = 0
while start <= end:
    mid = (start + end) // 2
    if divide(mid) <= m:
        end = mid - 1
        result = mid
    else: # mid를 이용해서 나온 결과값이 많다는거야, 즉 mid가 너무 작으니까 구간이 너무 많이 나눠진거야 그러니까 start를 키워줘야지
        start = mid + 1
print(result)



# 최댓값의 최소를 너무 작하니까 구간이 너무 작아졌어
# 최댓값의 최소를 적당히 하니까 m보다 작아졌어
