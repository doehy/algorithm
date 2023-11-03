n = int(input())

data = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = data[1] # 카드를 한개를 샀을 때의 최댓값은 data의 값이 들어가있을 때이다.
for i in range(2,n+1): # i가 2부터 n까지의 최댓값을 구할 것이니
    for k in range(i,0,-1): # k는 이제 그 전 숫자들을 골랐을 때이다.
        if dp[i] < dp[i-k] + data[k]: 
            dp[i] = dp[i-k] + data[k]
print(dp[n])