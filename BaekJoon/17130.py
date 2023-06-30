import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
sr, sc = 0,0
for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] == 'R':
            sr,sc = i,j
    graph.append((temp))
dp = [[-1] * m for _ in range(n)]
dp[sr][sc] = 0 
dx = [-1,0,1]
dy = [-1,-1,-1]
def isRange(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False
flag = 0
count = 0
for j in range(sc+1,m): #여까지는 누구나 생각함
    for i in range(0,n):
        if graph[i][j] == '#':
            continue
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if isRange(nx,ny) and dp[nx][ny] != -1:
                if graph[i][j] == 'C':
                    dp[i][j] = max(dp[i][j], dp[nx][ny] + 1)
                if graph[i][j] == '.':
                    dp[i][j] = max(dp[i][j], dp[nx][ny])
                if graph[i][j] == 'O': # 당근을 하나도 안 들고 탈출할 수도 있는 거잖아 그치?
                    flag = 1
                    dp[i][j] = max(dp[i][j], dp[nx][ny])
                    count = max(count, dp[i][j])
            
if flag == 0:
    print(-1)
else:
    print(count)

# 토끼가 있는 곳 부터 출발?