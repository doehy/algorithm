import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
num = min(n,m) // 2
def checkUp(count):
    temp = data[count][m-1-count]
    for i in range(m-1-count, count, -1): # 4-1-0 0-1  3 -1 3 0
        tp = data[count][i-1]
        data[count][i-1] = temp
        temp = tp
def checkRight(count):
    temp = data[n-1-count][m-1-count] # 3 3
    for i in range(n-1-count, count, -1): # 4-1-0, 0-1  3 -1 3 0
        tp = data[i-1][m-1-count]  # 2 3 1 3 0 3
        data[i-1][m-1-count] = temp
        temp = tp
def checkDown(count):
    temp = data[n-1-count][count] # 3 0
    for i in range(count, m-1-count): # 0 4-1-0 , 0 3
        tp = data[n-1-count][i+1]
        data[n-1-count][i+1] = temp
        temp = tp
def checkLeft(count):
    temp = data[count][count] # 0 0
    for i in range(count, n-count-1): # 0, 4-0
        tp = data[i+1][count]
        data[i+1][count] = temp
        temp = tp

for i in range(num):
    for j in range(r):
        temp = data[i][i]
        checkUp(i)
        checkRight(i)
        checkDown(i)
        checkLeft(i)     
        data[i+1][i] = temp

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()

# 한 줄로 이어붙여 보기