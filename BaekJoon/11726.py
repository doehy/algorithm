#첫 생각이 맞았고 n이 4일 때의 경우를 잘 못 구해 헛 돌았다.

n = int(input())

dp = [0] * 1001

def dynamic(n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    dp[5] = 8
    dp[6] = 13

    for i in range(7,n+1):
        dp[i] = dp[i-1] + dp[i-2]

dynamic(n)
print(dp[n] % 10007)