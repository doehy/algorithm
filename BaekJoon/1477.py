import sys
input = sys.stdin.readline
n,m,l = map(int,input().split())
data = [0] + list(map(int,input().split())) + [l]
data.sort()
left, right = 1, l-1
answer = 0
while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in range(len(data)-1):
        temp += (data[i+1] - data[i] - 1) // mid 
    if temp > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)