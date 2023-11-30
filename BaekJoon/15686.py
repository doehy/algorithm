from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

chicken = []
s = []
home = []
result = []

def cal(s):
    global home
    temp = []
    for num,s_x,s_y in s:
        for h_x,h_y in home:
            temp.append(abs(s_x-h_x) + abs(s_y-h_y))
    sum = 0
    for i in range(len(home)):
        min_num = float("inf")
        while i < len(home) * len(s):
            min_num = min(min_num,temp[i])
            i += len(home)
        sum += min_num
    result.append(sum)            

def check(s,m,chicken,home):
    if len(s) == m:
        cal(s)
        return
    else:
        if len(s) == 0:
            for i in chicken:
                s.append(i)
                check(s,m,chicken,home)
                s.pop()
        else:
            for num,x,y in chicken:
                if num > s[len(s)-1][0]:
                    s.append([num,x,y])
                    check(s,m,chicken,home)
                    s.pop()


num = 0

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            num += 1
            chicken.append([num,i,j])
        if data[i][j] == 1:
            home.append([i,j])

check(s,m,chicken,home)
print(min(result))