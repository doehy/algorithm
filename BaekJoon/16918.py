import sys
input = sys.stdin.readline
r,c,n, = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
isgraph = set([(i,j) for i in range(r) for j in range(c)])
if n == 1:
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print()
else:
    if n % 2 == 0:
        for i in range(r):
            for j in range(c):
                print('O', end='')
            print()
    else:
        zero = set()
        one = set()
        two = set()
        temp = set()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]    
        for i in range(r):
            for j in range(c):
                if graph[i][j] == '.':
                    zero.add((i,j))
                else:
                    two.add((i,j))    
        for i in range(n-2): # n이 2초면 아에 이 반복에 안 들어갈 것이고 n이 3초면 한 번 반복 ok
            if i % 2 == 0:
                temp = set()
                for x,y in two:
                    temp.add((x,y))
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            temp.add((nx,ny))
                zero = zero - temp # 이러면 zero에 있던 폭탄들중에서도 해당되는 것들은 터졌다.
                one = zero # 이제 0초가 1초가 된다..
            else:
                two = one
                zero = isgraph - one # 전체에서 2초를 뺀것이 이제 0초가 된다.
        for i in range(r):
            for j in range(c):
                if (i,j) in one:
                    print("O", end='')
                else:
                    print(".", end='')
            print()
