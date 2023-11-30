n = int(input())

visited = [[0] * 101 for _ in range(101)]

dx = [((0),(-1),(0),(1)),((0,-1),(-1,0),(0,1),(1,0)),((0,-1,0,-1),(-1,0,1,0),(0,1,0,1),(1,0,-1,0)),((0,-1,0,-1,0,1,0,-1),(-1,0,1,0,1,0,1,0),
                                                                                            (0,1,0,1,0,-1,0,1),(1,0,-1,0,-1,0,-1,0))] # 이게 행 개념
dy = [((1),(0),(-1),(0)),((1,0),(0,-1),(-1,0),(0,1)),((1,0,-1,0),(0,-1,0,-1),(-1,0,1,0),(0,1,0,1)),((1,0,-1,0,-1,0,-1,0),(0,-1,0,-1,0,1,0,-1),
                                                                                            (-1,0,1,0,1,0,1,0),(0,1,0,1,0,-1,0,1))] # 이게 열 개념

for i in range(n): 
    c,r,d,g = map(int,input().split())
    visited[r][c] = 1

    for i in range(2**g):
        print(g,d,i)
        r += dx[g][d][i] 
        c += dy[g][d][i]
        visited[r][c] = 1
count = 0
for i in range(0,100):
    for j in range(0,100):
        if visited[i][j] == 1 and visited[i][j+1] == 1 and visited[i+1][j] == 1 and visited[i+1][j+1] == 1:
            count += 1
print(count)