t = int(input())

def DFS(x,y):
    if x < 0 or x > m-1 or y < 0 or y>n-1:
        return False
    if graph[x][y] == 0 or visited[x][y] == 1:
        return False
    else:
        visited[x][y] = 1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True


for p in range(t):
    result = 0
    visit = []
    graph = []
    m,n,k = map(int,input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for i in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1
    for j in range(m):
        for u in range(n):
            if DFS(j,u) == True:
                result += 1
    print(result)
