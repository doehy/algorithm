n = int(input())
box = list(map(int,input().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i],dp[j]+1) # 앞에 있던겁소다 크면 거기서 + 1
    print(dp)

print(max(dp)) # 마지막 상자에 들어있는 것이 최댓값이 아닐 수도 있다.