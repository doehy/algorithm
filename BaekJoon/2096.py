# 메모리 제한 때문에 1차원 배열로 풀었어야 했다.
# 슬라이딩 윈도우 기법도 있따. 슬라이딩 기법으로 풀면 더 간단하게 풀 수 있다. 나중에 다시 왔을 때 슬라이딩으로 풀어보자 지금 이건 dp다

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a,b,c = map(int,input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j],max_dp[j+1])
            min_tmp[j] = a + min(min_dp[j],min_dp[j+1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j-1],max_dp[j],max_dp[j+1])
            min_tmp[j] = b + min(min_dp[j-1],min_dp[j],min_dp[j+1])
        else:
            max_tmp[j] = c + max(max_dp[j],max_dp[j-1])
            min_tmp[j] = c + min(min_dp[j],min_dp[j-1])
    for k in range(3):
        max_dp[k] = max_tmp[k]
        min_dp[k] = min_tmp[k]

print(max(max_dp), min(min_dp))