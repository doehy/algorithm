n = int(input())

data = list(map(int,input().split()))

m = int(input())
data.sort()
left, right = 0, data[-1] # left는 당연히 최소로 정해주지만 right는 제일 큰 값으로 정해줬다.
result = 0
while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in data:
        if mid > i:
            temp += i
        else:
            temp += mid
        if temp > m:
            break
    if temp > m: # temp가 예산 보다 많았다면 상한액을 너무 높이 정한거니 right를 줄인다. # 많으면 답이 될 수 없으니
        right = mid - 1 
    else: # 여기로 간다. 답도 여기 있을 것 이다.
        left = mid + 1
        result = mid
    
print(result)
# 일단 m을 n으로 나눠서 평균을 구하고 거기서 아래로 내려가거나 위로 올라가면 되는데 이렇게 하면 data의 최대가 만이니 시간초과
# 이분탐색을 이용해서 탐색 범위를 반 씩 줄인다면 시간초과가 안 난다.
