import sys
input = sys.stdin.readline
r,c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 1
def solve(x,y,alpha,cur):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] in alpha:
                ans = max(ans, cur)
            else:
                alpha.add(graph[nx][ny])
                solve(nx,ny,alpha, cur + 1)
                alpha.remove(graph[nx][ny])
temp = set()
temp.add(graph[0][0])
solve(0,0,temp,1)
print(ans)
