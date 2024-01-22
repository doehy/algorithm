import sys
input = sys.stdin.readline
n,g,k = map(int,input().split())
d1 = []
d2 = []
for _ in range(n):
    s,d,o = map(int,input().split())
    if o:
        d1.append([s,d])
    else:
        d2.append([s,d])

result = 0
left, right = 0, 2*(10**9) # 날짜 0일부터 시작해야하나? 
while left <= right:
    mid = (left + right) // 2
    temp_g = 0
    if len(d1) > k:
        d1.sort(key=lambda x:(-x[0] * max(1,(mid - x[1]))))
        for i in range(k, len(d1)):
            temp_g += d1[i][0] * max(1,(mid - d1[i][1]))
    for i in range(len(d2)):
        temp_g += d2[i][0] * max(1,(mid - d2[i][1]))
    if temp_g > g:
        right = mid - 1
    else:
        left = mid + 1
        result = mid
print(result)


# 부패 속도가 빨라봤자 유통기한이 길다면 아무 의미가 없다.
# 유통기한이 짧다면 바로 부패가 시작될 것이다. 이 때는 부패가 속도가 빠른 것을 없애야 한다. 
# 위에서 변수가 있다는 것은 알았다. 그래서 그것을 배려해서 시간 제한이 2초로 주어졌다. 즉 정렬을 한번만 안해도 된다는 뜻이다.
# right를 정하는 최악의 기준이 왜 아직도 2e9인지 모르겠다.