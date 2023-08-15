import sys
input = sys.stdin.readline
first = input().rstrip()
second = input().rstrip()
h,w = len(first), len(second)
dp = [[0] * (w+1) for _ in range(h+1)]

for i in range(1,h+1):
    for j in range(1, w+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[h][w])

