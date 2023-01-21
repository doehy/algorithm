import sys, math
input = sys.stdin.readline

n,m = map(int,input().split())
data = []
for i in range(m):
    data.append(int(input()))

left, right = 1,max(data)
answer = 0

while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in data:
        temp += math.ceil(i/mid)
    if temp > n:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
