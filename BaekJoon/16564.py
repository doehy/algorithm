import sys
input = sys.stdin.readline

n,k = map(int,input().split())

data = []

min_num = float("inf")
max_num = 0

for i in range(n):
    num = int(input())
    data.append(num)
    min_num = min(min_num, num)
    max_num = max(max_num,num)

data.sort()

left, right = min_num, min_num + k
result = 0
while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in data:
        if i > mid:
            break
        temp += mid - i
        if temp > k:
            break
    if temp > k:
        right = mid - 1
    else:
        left = mid + 1
        result = mid

print(result)