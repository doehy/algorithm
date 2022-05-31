import sys
input = sys.stdin.readline

n,q = map(int,input().split())

visited = [0] * (n+1)

flag = 0

for k in range(q):
    i = int(input())
    temp = i
    tmp = 0
    while i != 1:
        if visited[i]: 
            flag = 1
            tmp = i
        i //= 2 
    if flag:
        print(tmp)
        flag = 0
    else:
        visited[temp] = 1
        print(0)
    



