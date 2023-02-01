from collections import deque

T = int(input())
data = []
for _ in range(T):
    data.append(deque(input()))
K = int(input())
# 1이 오른쪽 회전(시계방향)-1이 왼쪽으로 회전
for i in range(K):
    num, dif = map(int,input().split())
    md = dif # 처음 방향을 기억해놓을라고
    num -= 1 # idx는 0부터 시작이니까 1을 빼줌
    mnum = num # 처음 숫자를 기억해놓을라고
    temp = dict() # 매 반복마다 새로운 사전형을 만들 것이다.
    while num > 0: # 자신보다 작은 톱니바퀴에 다가가는 것이다.
        if data[num][6] == data[num-1][2]: # 일단 달라야 회전시키고 뭘 하는데 같아지는 순간 톱니바퀴는 돌아가지 않는다.
            break 
        else: # 맞닿은 톱니바퀴의 번호가 다르다
            # 지금 돌리면 안 된다. 한 번에 돌려야 되는데
            if num not in temp:
                temp[num] = dif
            if num-1 not in temp:
                temp[num-1] = -1 * dif
            dif *= -1 # 회전방향은 -1씩 변하니까
            num -= 1 # 전 톱니바퀴로 다가가기 위해서 -1을 해준다.
    dif = md # 처음 방향을 다시 집어넣어준다.
    num = mnum
    while num < T-1:
        if data[num][2] == data[num+1][6]: # 일단 달라야 회전시키고 뭘 하는데 같아지는 순간 톱니바퀴는 돌아가지 않는다.
            break 
        else: # 맞닿은 톱니바퀴의 번호가 다를경우
            if num not in temp:
                temp[num] = dif
            if (num+1) not in temp:
                temp[(num+1)] = (-1 * dif)
            num += 1
            dif *= -1
    for j in temp.keys():
        data[j].rotate(temp[j])
    if len(temp.keys()) == 0:
        data[mnum].rotate(md)

count = 0

for i in range(T):
    if data[i][0] == '1':
        count += 1

print(count)

