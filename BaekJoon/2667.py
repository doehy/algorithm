n = int(input())

graph = []

home_num = 0 #번지 수
cnt = 0 #번지 별 들어갈 집 개수
home = [] #집 주소

for i in range(n):
    graph.append(list(map(int,input())))

def DFS(x,y):
    global cnt
    if x<0 or x > n-1 or y <0 or y > n-1:
        return False
    if graph[x][y] == 0:
        return False
    else:
        graph[x][y] = 0
        cnt += 1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True

for j in range(n):
    for k in range(n):
        if DFS(j,k) == True:
            home.append(cnt)
            home_num += 1
            cnt = 0

print(home_num)
home.sort()
number = len(home)
for u in range(number):
    print(home[u])

