from collections import deque

n,m,cnt = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
number = list(map(int,input().split()))

def one_rotate(data):
    temp = deque([])
    for i in range(n):
        temp.append(data.pop())
    for i in range(n):
        data.append(temp.popleft())

def two_rotate(data):
    temp = deque([])
    for j in range(m):
        lis = list()
        for i in range(n):
            lis.append(data[i][j])
        temp.appendleft(lis)
    for j in range(m):
        for i in range(n):
            data[i][j] = temp[j][i]

def three_rotate(data):
    global m
    global n
    temp = deque([])
    for j in range(m):
        lis = list()
        for i in range(n-1,-1,-1):
            lis.append(data[i][j])
        temp.append(lis)
    for i in range(n):
        data.pop()
    for k in temp:
        data.append(k)
    n,m = m,n # 90도 돌아가니 행과열의 길이가 바뀔 것이다.

def four_rotate(data):
    global n
    global m
    temp = deque([])
    for j in range(m-1,-1,-1):
        lis = list()
        for i in range(n):
            lis.append(data[i][j])
        temp.append(lis)
    for i in range(n):
        data.pop()
    for k in temp:
        data.append(k)
    n,m = m,n

def five_rotate(data):
    temp = deque([])
    for i in range(n//2):
        lis = list()
        for j in range(m//2):
            lis.append(data[i][j])
        temp.append(lis)
    
    for i in range(n//2):
        lis = list()
        for j in range(m//2,m):
            lis.append(data[i][j])
        temp.append(lis)
    
    for i in range(n//2,n):
        lis = list()
        for j in range(m//2):
            lis.append(data[i][j])
        temp.append(lis)
    
    for i in range(n//2,n):
        lis = list()
        for j in range(m//2,m):
            lis.append(data[i][j])
        temp.append(lis)

    ti , tj = 0,0
    for i in range(n):
        tj = 0
        for j in range(m//2,m):
            data[i][j] = temp[ti][tj]
            tj += 1
        ti += 1

    for i in range(n):
        tj = 0
        for j in range(m//2):
            data[i][j] = temp[ti][tj]
            tj += 1
        ti += 1
def six_rotate(data):
    temp = deque([])
    for i in range(n//2,n):
        lis = list()
        for j in range(m//2,m):
            lis.append(data[i][j])
        temp.append(lis)
    for i in range(n//2,n):
        lis = list()
        for j in range(m//2):
            lis.append(data[i][j])
        temp.append(lis)
    for i in range(n//2):
        lis = list()
        for j in range(m//2,m):
            lis.append(data[i][j])
        temp.append(lis)
    for i in range(n//2):
        lis = list()
        for j in range(m//2):
            lis.append(data[i][j])
        temp.append(lis)

    ti , tj = 0,0
    for i in range(n):
        tj = 0
        for j in range(m//2,m):
            data[i][j] = temp[ti][tj]
            tj += 1
        ti += 1

    for i in range(n):
        tj = 0
        for j in range(m//2):
            data[i][j] = temp[ti][tj]
            tj += 1
        ti += 1

for i in number:
    if i == 1:
        one_rotate(data)
    if i == 2:
        two_rotate(data)
    if i == 3:
        three_rotate(data)
    if i == 4:
        four_rotate(data)
    if i == 5:
        five_rotate(data)
    if i == 6:
        six_rotate(data)