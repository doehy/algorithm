#고민을 게속 해봤지만 계속 틀렸다 도무지 모르겠어서 검색해봤더니
#현재 포도주를 마시지 않는 경우도 고려해줬어야 했다. 음 뭔가 이 생각을 안 했던 것은 아니다
#이 생각을 했었지만 최댓값을 구해야한다는 생각에 마시지 않으면 손해라는 생각이 들어 결과에 다가갈 수 없었다.
#다음부터는 생각을 틀기 전에 정말 아닌 것인가라는 생각을 해야할 것 같다.

import sys
input = sys.stdin.readline

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))

dp = [0]
dp.append(w[1])
if n>1:
    dp.append(w[1]+w[2])
for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i]))
print(dp[n])




