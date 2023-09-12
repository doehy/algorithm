# 벼락치기
import sys
input = sys.stdin.readline
n,t = map(int,input().split())
dp = [0] * (t+1) # 아 이거 그냥 일차원이다 싯팔
for _ in range(n):
    k, s = map(int,input().split())
    for i in range(t, -1, -1):
        if i >= k: 
            dp[i] = max(dp[i-k] + s, dp[i]) # 여기서 dp[i]를 해야하는 이유는 택하지 않는게 최선일 수도 있따. 
        else: #  
            break 
print(dp[t])   



# 함께 블록 쌓기와 똑같은 문제이다.
# 모든 경우의 수를 파악해야하는 것 같지만 그렇게 할 경우 시간 초과다
# 또한 전에 내가 택한 경우에 대해서 앞으로의 영향을 미친다.
# 근데 다른 배낭과는 다르게 담았던 것을 또 담을 수는 없다 그렇기에 담거나 안 담거나이다. 그래서 처음에는 일차원 dp를 만들어서 풀었다.
# 일차원으로 하니 시간이 오래 걸리는 것 같아서 이차원으로도 한 번 풀어보겠다.
# 바로 밑에 코드가 이차원인데 이차원이 오히려 일차원보다 시간이 오래걸렸다. 직관적으로 단어만 보면 이차원이기 때문에 더 오래걸리긴 했지만
# 난 덜 걸릴 줄 알았다.




# import sys
# input = sys.stdin.readline

# N, T = map(int, input().rsplit())

# times, scores = [0], [0]

# for _ in range(N):
#     t, s = map(int, input().rsplit())
#     times.append(t)
#     scores.append(s)

# # i개의 단원을 j시간 동안 공부했을 때 얻을 수 있는 최대 점수
# dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, T+1):
#         if j >= times[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i]] + scores[i])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[N][T])