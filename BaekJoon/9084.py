import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int,input().split()))
    coin.insert(0, 0)
    target = int(input())

    dp = [[0] * (target + 1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):    
            dp[i][j] = dp[i-1][j]
            if j - coin[i] >= 0:
                dp[i][j] += dp[i][j-coin[i]]
    print(dp[n][target])

# 이거 그냥 해당 동전으로 target지점까지
# 돈으로 0원을 만드는 방법은 생각해보면 1가지다.(근데 이 부분은 문제를 풀면서 필요하다고 생각하면 추가하면 된다.)
# 최댓값만을 계속 구해가기 떄문에 dp[i][j] = dp[i-1][j] 해당 목표값만을 만드는 데 필요한 경우의 수는 직전 작은 돈에서 구한 값을 일단 가져온다.
# 그리고 이 동전을 쓸 수 있다면 쓰기전에서 구한 값에 더하면 된다. 
# 나는 처음에는 나머지를 구했는데 이걸 왜 생각했지..... 