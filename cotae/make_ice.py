from pickle import FALSE


N,M = map(int,input().split())

graph = []

for i in range(N):
    graph.append(list(map(int,input())))

def make_ice(x,y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return FALSE
    if graph[x][y] == 1:
        return FALSE
    else:
        graph[x][y] = 1
        make_ice(x-1,y)
        make_ice(x+1,y)
        make_ice(x,y-1)
        make_ice(x,y+1)
        return True
    
num = 0

for i in range(N):
    for j in range(M):
        if make_ice(i,j)==True:
            num += 1

print(num)
