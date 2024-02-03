import sys
input = sys.stdin.readline
scroll = list(input().rstrip())
devil = list(input().rstrip())
angel = list(input().rstrip())
ans = 0
lens = len(scroll)
lenb = len(devil)
bridge = [devil, angel]
def sol(start_bridge_type):
    global ans
    dp = [[[0 for _ in range(lens)] for _ in range(lenb)] for _ in range(2)]
    curr_bridge = start_bridge_type

    for i in range(lenb):
        if scroll[0] == bridge[curr_bridge][i]:
            dp[curr_bridge][i][0] = 1

    curr_bridge = (curr_bridge + 1) % 2

    for i in range(1,lens):
        for j in range(lenb):
            if scroll[i] == bridge[curr_bridge][j]:
                before_bridge = (curr_bridge + 1) % 2

                for k in range(j):
                    if scroll[i-1] == bridge[before_bridge][k]:
                        dp[curr_bridge][j][i] += dp[before_bridge][k][i-1]
        curr_bridge = (curr_bridge + 1) % 2

    for i in range(lenb): 
        ans += dp[0][i][lens-1]
        ans += dp[1][i][lens-1]

sol(0)  # 악마 다리부터 시작
sol(1)  # 천사 다리부터 시작
print(ans)
