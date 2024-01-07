import sys
input = sys.stdin.readline
n,k,t = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
temp = []
seq = 0
flag = 0
while seq < n:
    if k < 1:
        break
    if t <= data[seq]: # 내가 지금은 못 먹어 나보다 이상이라
        while t <= data[seq]:
            if len(temp) <= 0 or k < 1:
                flag = 1
                break 
            t += temp[-1]
            k -= 1 
            temp.pop()
        if t > data[seq]:
            temp.append(data[seq])
            seq += 1
    elif t > data[seq] and k >= 1: # 현재 나보다 몸집이 작고 먹을 기회가 한 번이상 있으면
        temp.append(data[seq])
        seq += 1
    if flag == 1:
        break

while len(temp) > 0 and k > 0:
    t += temp[-1]
    temp.pop()
    k -= 1
print(t)