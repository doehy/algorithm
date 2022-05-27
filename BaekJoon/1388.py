n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

result = 0

def dfs(x,y):
    text = graph[x][y]
    graph[x][y] = 0
    if text == '-':
        if y+1 < m and graph[x][y+1] == '-':
            dfs(x,y+1)
            return
    if text == '|':
        if x+1 < n and graph[x+1][y] == '|':
            dfs(x+1,y)
            return

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            dfs(i,j)
            result += 1

print(result)