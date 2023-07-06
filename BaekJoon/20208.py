import sys
input = sys.stdin.readline
n,m,h = map(int,input().split())
data = []
mint = []
sr,sc = 0,0
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 1:
            sr,sc = i,j
        elif temp[j] == 2:
            mint.append((i,j))
    data.append(temp)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [0] * len(mint)
ans = 0
def solve(x,y,hp,count):
    global ans 
    for i in range(len(mint)):
        if not visited[i]:
            temp = abs(mint[i][0] - x) + abs(mint[i][1] - y)
            if hp >= temp: 
                visited[i] = 1
                solve(mint[i][0],mint[i][1],hp-temp+h,count+1)
                visited[i] = 0
    if hp >= abs(sr-x) + abs(sc-y):
        ans = max(ans,count)

solve(sr,sc,m,0)
print(ans)