n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

data = []
cnt = 0
picture = 0

def paint(x,y):
    global cnt
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    if graph[x][y] == 0:
        return False
    else:
        cnt += 1
        graph[x][y] = 0
        paint(x-1,y)
        paint(x+1,y)
        paint(x,y-1)
        paint(x,y+1)
        return True

for i in range(n):
    for j in range(m):
        if paint(i,j) == True:
            picture += 1 # 그림의 개수로 출력될 것
            data.append(cnt)
            cnt = 0


print(picture)
print(max(data) if data else 0)