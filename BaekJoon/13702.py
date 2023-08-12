n,k = map(int,input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()

left, right = 1, data[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for num in data:
        count += num // mid
    if count >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)