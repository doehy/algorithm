n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
left, right = 1,data[-1]
result = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(len(data)-1,-1,-1):
        if data[i] < mid:
            break
        count += data[i] // mid
    if count >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

# 사람수보다 부족하면 오케이 이렇게 하면 되겠다.
