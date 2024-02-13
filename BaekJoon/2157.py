import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
data = [[] for _ in range(n+1)]

for _ in range(k):
    a,b,grade = map(int,input().split())
    if a < b:
        data[a].append([b,grade])

dp = [[-1] *(m+1) for _ in range(n+1)]# 좌표, 몇 점, 몇 개만에 해당 지역으로 왔는지
dp[1][1] = 0
visited = [0] * (n + 1)
visited[1] = 1

for i in range(1, n): # 최대 300
    if not visited[i]:
        continue 
    for j in range(len(data[i])): # 최대 십만
        for k in range(1, i+1): # 최대 300, 다시 돌아오는 이유가 없기 때문에 현재 내 좌표보다 많은 경우의 수를 경유해서 왔을 수 없기 때문에 내가 최대다
            if k == m:
                break
            visited[data[i][j][0]] = 1
            dp[data[i][j][0]][k + 1] = max(dp[data[i][j][0]][k + 1], dp[i][k]+ data[i][j][1]) 
ans = 0

for grade in dp[n]:
    ans = max(ans, grade)
print(ans)


# 모든 경우의 수를 세야한다. 여행지는 최대 300개, 경로가 최대 십만 개, 맨 처음에는 dfs로 풀라고 했는데 사실 이건 dfs가 아니지
# 지역마다 점수가 있다. 최대한 빠르게 가는 길을 찾는게 아니잖아 최대한 빠르게 가는데 몇초가 걸리는 것을 찾는게 아니잖아
# m개 지역 이하를 이용해 최대 점수를 얻어야 하는 거니가 이건 dp이다.
