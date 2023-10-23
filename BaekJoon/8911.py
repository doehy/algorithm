import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    dif = list(input())
    x,y = 0,0
    see = 0
    max_x  = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for j in range(len(dif)):
        if dif[j] == 'F':
            if see % 4 == 0:
                x,y = x-1,y
                max_x = max(max_x,x)
                min_x = min(min_x,x)
            elif see % 4 == 1:
                x,y = x,y+1
                max_y = max(max_y,y)
                min_y = min(min_y,y)
            elif see % 4 == 2:
                x,y = x+1,y
                max_x = max(max_x,x)
                min_x = min(min_x,x)
            else:
                x,y = x,y-1
                max_y = max(max_y,y)
                min_y = min(min_y,y)
        elif dif[j] == 'L':
            see -= 1
        elif dif[j] == 'R':
            see += 1
        elif dif[j] == 'B':
            if see % 4 == 0:
                x,y = x+1,y
                max_x = max(max_x,x)
                min_x = min(min_x,x)
            elif see % 4 == 1:
                x,y = x,y-1
                max_y = max(max_y,y)
                min_y = min(min_y,y)
            elif see % 4 == 2:
                x,y = x-1,y
                max_x = max(max_x,x)
                min_x = min(min_x,x)
            else:
                x,y = x,y+1
                max_y = max(max_y,y)
                min_y = min(min_y,y)

    
    print((max_x - min_x) * (max_y - min_y))
