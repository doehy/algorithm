from collections import deque
import sys
input = sys.stdin.readline
n,a,b = map(int,input().split())
dp = [float("inf")] * 1000001
dp[n] = 0
for i in range(n,-1,-1):
    if i-1 >= 0: dp[i-1] = min(dp[i-1], dp[i] + 1)
    if i-a-1 >= 0: dp[i-a-1] = min(dp[i-a-1], dp[i] + 1)
    if i-b-1 >= 0: dp[i-b-1] = min(dp[i-b-1], dp[i] + 1) 
print(dp[0])

