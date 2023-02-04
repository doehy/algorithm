N = int(input())
S = list(map(int,input().split()))
# N 이 최대 20개 dfs로 짜면 약 백만이기에 근데 시간제한이 2초니까 타이트하게 짜면 통과할 수도 있겠다.
# 지금 생각하는게 수열을 정렬을 하고 구해가자
S.sort()
dp = [0] * (sum(S)+1)

def check(idx,total,dp):
    dp[total] = 1
    if idx == len(S):
        return
    check(idx+1,total+S[idx],dp) # 선택하는 것
    check(idx+1,total,dp) # 선택안하는 것

dp[S[0]] = 1
check(0,0,dp)
flag = 0
for i in range(1,len(dp)):
    if dp[i] == 0:
        print(i)
        flag = 1
        break
if flag == 0:
    print(sum(S)+1)
