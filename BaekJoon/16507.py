r,c,q = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(r)]

sumd = [[0] * (c+1) for i in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        sumd[i][j] = data[i-1][j-1] + sumd[i-1][j] + sumd[i][j-1] - sumd[i-1][j-1]

for i in range(q):
    x1, y1, x2, y2 = map(int,input().split())
    print((sumd[x2][y2] + sumd[x1-1][y1-1] - sumd[x1-1][y2] - sumd[x2][y1-1]) // ((x2 + 1 - x1) * (y2 + 1 - y1)))