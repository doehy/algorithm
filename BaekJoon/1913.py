n = int(input())

number = int(input())

graph = [[0] * n for _ in range(n)]

graph[0][0] = n ** 2

def check(x,y):
    p = q = 0
    start = 0
    global n 
    global number
    final = n ** 2 - 1   
    while final != 0:
        if start == 0:
            while x+1 < n and graph[x+1][y] == 0 :
                if final == number:
                    p,q = x+1,y
                graph[x+1][y] = final
                final -= 1            
                x += 1
            start = 1
        if start == 1:
            while y+1 < n and graph[x][y+1] == 0:
                if final == number:
                    p,q = x,y+1
                graph[x][y+1] = final
                final -= 1
                y += 1
            start = 2
        if start == 2:
            while x-1 >= 0 and graph[x-1][y] == 0:
                if final == number:
                    p,q = x-1,y
                graph[x-1][y] = final
                final -= 1
                x -= 1
            start = 3
        if start == 3:
            while y-1 >= 0 and graph[x][y-1] == 0:
                if final == number:
                    p,q = x,y-1
                graph[x][y-1] = final
                final -= 1
                y -= 1
            start = 0
    return p+1,q+1

result_x,result_y = check(0,0)

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=' ')
    print()

print(result_x,result_y)



