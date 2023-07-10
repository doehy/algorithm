import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
if n == 1:
    if data[0] > m:
        print(0)
    else:
        print(data[0])
else:
    temp = 0
    ans = 0
    l,r = 0,1
    temp += data[l]
    while l <= r and r < n: 
        if data[r] <= m - temp: # 만약 data[r]보다 크거나 같아 그럼 더할 수 있는거니까
            temp += data[r] # 더해
            r += 1# 그리고 r만 증가시켜
        else: # 근데 만약 data[r]이 더 크면 l을 빼야지
            if l == r: # l이 r과 같다는 의미는 현재 idx가 혼자만으로도 너무 크니까
                l += 1 #l,r을 하나씩 증가시키고 temp도 0으로 만들어
                r += 1
                temp = 0
                continue
            temp -= data[l] #temp에서 data[l]을 빼
            l += 1 # l을 1증가시
        ans = max(ans,temp)
    print(ans)
