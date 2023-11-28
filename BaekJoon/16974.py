N, X = map(int, input().split())

dp = [1] * 51            # 버거의 레이아웃 갯수
paeti = [1] * 51             # 버거의 패티 갯수


for i in range(1, N+1):
    dp[i] = 1 + dp[i-1] + 1 + dp[i-1] + 1
    paeti[i] = paeti[i-1] + 1 + paeti[i-1]

def solve(cn, cx):
    if cn == 0:
        return cx
    if cx == 1: # 0이었으면 위에서 걸러지는데 0이 아니었는데 1이었다는 것은 패티가 추가가 안 됨
        return 0
    elif cx <= 1 + dp[cn-1]:
        return solve(cn -1, cx-1)
    elif cx == 1 + dp[cn-1] + 1:
        return paeti[cn-1] + 1
    elif cx <= dp[cn-1] + dp[cn-1] + 1 + 1:
        return paeti[cn-1] + 1 + solve(cn-1,cx - (dp[cn-1] + 2))
    else:
        return paeti[cn]    

print(solve(N,X))
