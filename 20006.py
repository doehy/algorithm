# 20006 랭킹전 대기열
from collections import defaultdict
import sys
input = sys.stdin.readline
p,m = map(int,input().split())
matching = dict()
lv, name = input().rstrip().split()
lv = int(lv)
matching[(lv, name)] = [1, [[lv, name]]]

for _ in range(p-1):
    flag = 0 # 매번 방은 새로 파면 안 되고 조건이 만족할 때 방을 새로 파는거야
    lv, name = input().rstrip().split()
    for i in matching.keys():
        if i[0] - 10 <= int(lv) <= i[0] + 10:
            if matching[i][0] < m:
                matching[i][0] += 1
                matching[i][1].append([int(lv), name])
                flag = 1
                break
    if flag == 0: # matching 되는게 없었으면 방을 새로 파야하니까
        matching[(int(lv), name)] = [1, [[int(lv), name]]]


for i in matching.keys():
    matching[i][1].sort(key = lambda x:x[1])

for i in matching.keys():
    if matching[i][0] == m:
        print("Started!")    
    else:
        print("Waiting!")
    for lis in matching[i][1]:
        print(*lis)