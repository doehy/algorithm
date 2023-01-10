n,m = map(int,input().split()) # n 강의의 수 m개의 블루레이

data = list(map(int,input().split())) # data를 입력받는다.

left,right = max(data),sum(data) # 최소는 data길이중 최대이고 최대는 data총합 길이만큼만 들어갈 수 있다.

result = 0 # 결과값은 0이다.

while left <= right: # left가 right보다 작거나 같은 동안
    mid = (left + right) // 2 
    cnt = 1
    flag = 0
    tempsum = 0 #tempsum은 계속 0으로 초기화 될 것임
    for i in range(len(data)):
        tempsum += data[i] # tempsum에 data[i] 값을 넣어준다.
        if tempsum > mid: # tempsum이 현재 블루레이 길이보다 크다면
            tempsum = data[i] # tempsum에다가 data[i]를 넣는다.
            cnt += 1 # 블루레이 갯수를 하나 증가시켜준다.
            if cnt > m: 
                left = mid+1
                flag = 1
                break
    if cnt==mid and tempsum > mid:
        left = mid + 1
        continue
    if flag == 0:
        result = mid
        right = mid - 1
    
print(result)