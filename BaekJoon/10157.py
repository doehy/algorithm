c,r = map(int,input().split())

number = int(input())

graph = [[0] * r for _ in range(c)]

def check(x,y):
    global c,r,number
    p = q = 0
    start = 0
    final = 1
    graph[x][y] = final
    while final != r*c:
        if start == 0:
            while y+1 < r and graph[x][y+1] == 0:
                final += 1
                if final == number:
                    p,q = x,y+1
                graph[x][y+1] = final
                y += 1
            start = 1
        if start == 1:
            while x+1 < c and graph[x+1][y] == 0 :
                final += 1
                if final == number:
                    p,q = x+1,y
                graph[x+1][y] = final
                x += 1
            start = 2
        if start == 2:
            while y-1 >= 0 and graph[x][y-1] == 0:
                final += 1
                if final == number:
                    p,q = x,y-1
                graph[x][y-1] = final
                y -= 1
            start = 3
        if start == 3:
            while x-1 >= 0 and graph[x-1][y] == 0:
                final += 1
                if final == number:
                    p,q = x-1,y
                graph[x-1][y] = final
                x -= 1
            start = 0
    if number == 1:
        print(1,1)
    else:
        if p==0 and q==0:
            print(0)
        else:
            print(p+1,q+1)

check(0,0)


                


                

               