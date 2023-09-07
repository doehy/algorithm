import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
white = 0
blue = 0

def check(x, y, fin):
    global white
    global blue
    color = graph[x][y]
    for i in range(x, x+fin):
        for j in range(y, y+fin):
            if graph[i][j] != color:
                check(x, y, fin // 2)
                check(x, y+fin//2, fin // 2)
                check(x+fin//2, y, fin // 2)
                check(x+fin//2, y+fin//2, fin // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1    

check(0,0,n)
print(white)
print(blue)
