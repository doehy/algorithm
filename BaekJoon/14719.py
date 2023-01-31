H,W = map(int,input().split())

data = list(map(int,input().split()))

count = 0

for i in range(1,W-1): # 양 옆은 탐색하지 않는다.
    left = max(data[:i])
    right = max(data[i+1:])

    compare = min(left,right)

    if data[i] < compare:
        count += compare - data[i]

print(count)     
