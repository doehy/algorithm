n = int(input())

data = list(map(int,input().split()))

dp = [float("inf")] * (n+1)
dp[1] = 0

for i in range(len(data)-1): # 마지막 발판은 어차피 이동못하기에 마지막 전 발판까지만 본다.
    for j in range(1,data[i]+1): #그 발판에서 이동할 수 있는 경우의 수를 반복문을 돌린다.
        if i+1+j <= n: #리스트의 범위를 벗어나지 않기 위해 if문을 작성한다.
            dp[i+1+j] = min(dp[i+1]+1,dp[i+1+j])


if dp[n] == float("inf"):
    print(-1)
else:
    print(dp[n])