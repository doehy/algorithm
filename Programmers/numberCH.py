def solution(x, y, n):
    answer = 0
    dp = [float("inf")] * (y+1)
    dp[x] = 0
    if x == y:
        return 0
    else:
    # dp로 가보자
        while x <= y:
            tp = x
            if tp * 3 <= y:
                dp[tp*3] = min(dp[tp*3],dp[x]+1)
            if tp * 2 <= y:
                dp[tp*2] = min(dp[tp*2],dp[x]+1)
            if tp + n <= y:
                dp[tp+n] = min(dp[tp+n],dp[x]+1)
            x = min(x * 2, x + n)
        if dp[y] == float("inf"):
            return -1
        answer = dp[y]
        return answer
print(solution(5,5,4))
