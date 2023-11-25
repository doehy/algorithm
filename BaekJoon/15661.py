from itertools import combinations
import math

n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

number = [i for i in range(n)]
min_num = float("inf")
flag = 0
def cal(li,temp):
    global min_num, flag
    li_sum, temp_sum = 0, 0
    if len(li) == 1:
        li_sum = li[0]
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            li_sum += data[li[i]][li[j]] + data[li[j]][li[i]]
    for i in range(len(temp) -1):
        for j in range(i+1, len(temp)):
            temp_sum += data[temp[i]][temp[j]] + data[temp[j]][temp[i]]
    total = abs(li_sum - temp_sum)
    if total == 0:
        flag = 1
        min_num = 0
    if total < min_num:
        min_num = total

def solve(li):
    temp = []
    for i in number:
        if i not in li:
            temp.append(i)
    cal(li, temp)
          
for i in range(1,math.ceil(n / 2) + 1):
    for li in combinations(number,i):
        solve(li)
        if flag == 1:
            break
    if flag == 1:
        break
print(min_num)