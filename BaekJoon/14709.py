n = int(input())

graph = []

flag = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))

if(n <= 2 or n >= 4):
    print("Woof-meow-tweet-squeek")
    flag = 2

if flag != 2:
    for a,b in graph:
        if (a == 1 and b == 3) or (a == 3 and b == 1):
            continue
        elif(a==3 and b == 4) or (a == 4 and b == 3):
            continue
        elif(a==1 and b==4) or (a==4 and b ==1):
            continue
        else:
            print("Woof-meow-tweet-squeek")
            flag = 1
            break

if flag != 1 and flag != 2:
    print("Wa-pa-pa-pa-pa-pa-pow!")
