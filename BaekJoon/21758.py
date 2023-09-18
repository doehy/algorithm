# 21758 꿀 따기
import sys
input = sys.stdin.readline
n = int(input())
honeys = list(map(int,input().split()))
answer = 0
def left(): # 꿀통이 제일 왼쪽에 있는 경우
    ret = 0
    dp = [0] * n
    for i in range(len(honeys)-2, -1, -1):
        dp[i] = dp[i+1] + honeys[i]
    for i in range(1,len(honeys)-1):
        ret = max(ret, (dp[0] - honeys[i]) + (dp[0] - dp[i]))   
    return ret

def right(): # 꿀통이 제일 오른쪽에 있는 경우
    ret = 0
    dp = [0] * n
    for i in range(1,len(honeys)):
        dp[i] = dp[i-1] + honeys[i]
    for i in range(1,len(honeys)-1):
        ret = max(ret, (dp[-1] - honeys[i]) + (dp[-1] - dp[i]))
    return ret

if n == 3:
    print(max(honeys) * 2)
else:
    answer = max(answer, left())
    answer = max(answer, right())
    print(answer)