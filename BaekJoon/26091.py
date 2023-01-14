n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
result = 0
left,right = 0,n-1
while left < right:
    if data[left] + data[right] >= m:
        result += 1
        left += 1
        right -= 1
    else:
        left += 1

print(result)