from collections import deque
# 1의 2번 2의 2번과 6번 3의 2번과 6번 4의 6번
# 1의 2번과 2의 6번 , 2의 2번과 3의 6번 , 3의 2번과 4의 6번 
data_1 = deque(input())
data_2 = deque(input())
data_3 = deque(input())
data_4 = deque(input())

k = int(input())

for i in range(k): # k만큼 반복문을 돌 것이다.
    num , dif = map(int,input().split()) # 돌릴 톱니바퀴 번호와 어느방향으로 돌릴지 입력받는다.
    flag_2 = 0 # 2번톱니바퀴에서 쓸 깃발이다.
    flag_3 = 0 # 3번톱니바퀴에서 쓸 깃발이다.
    if num == 1: # 1번 톱니바퀴로 시작할 것이다.
        if data_1[2] != data_2[6]: # 1번 톱니바퀴 2번과 2번 톱니바퀴 6번이 서로 다른 극인지  확인한다.
            data_1.rotate(dif) # 다르다면 1번 톱니바퀴를 입력받은 방향으로 회전시킨다.
            data_2.rotate(-dif)# 다르니 2번 톱니바퀴도 회전시키는데 1번과는 반대방향으로 회전시킨다.
            if data_2[2+-dif] != data_3[6]: #3번 톱니바퀴는 2번 톱니바퀴가 회전돼야 돌아갈 수 있으니 상위 if아래에 부속돼야 한다.
                data_3.rotate(dif) #2번은 이미 돌아갔으니 3번만 돌려준다. 
                if data_3[2+dif] != data_4[6]: #3번이 돌아가야 4번이 돌아갈 수 있으니 돌려준다.
                    data_4.rotate(-dif)
        else:
            data_1.rotate(dif)
    elif num == 2:
        if data_2[6] != data_1[2]:
            data_2.rotate(dif)
            data_1.rotate(-dif)
            flag_2 = 1
        if flag_2 == 1:
            if data_2[2+dif] != data_3[6]:
                data_3.rotate(-dif)
                if data_3[2 + -dif] != data_4[6]:
                    data_4.rotate(dif)
        if flag_2 == 0:
            if data_2[2] != data_3[6]:
                data_2.rotate(dif)
                data_3.rotate(-dif)
                if data_3[2 + -dif] != data_4[6]:
                    data_4.rotate(dif)
            else:
                data_2.rotate(dif)
    elif num == 3:
        if data_3[2] != data_4[6]:
            data_3.rotate(dif)
            data_4.rotate(-dif)
            flag_3 = 1
        if flag_3 == 1:
            if data_3[6+dif] != data_2[2]:
                data_2.rotate(-dif)
                if data_2[6 + -dif] != data_1[2]:
                    data_1.rotate(dif)
        if flag_3 == 0:
            if data_3[6] != data_2[2]:
                data_3.rotate(dif)
                data_2.rotate(-dif)
                if data_2[6 + -dif] != data_1[2]:
                    data_1.rotate(dif)
            else:
                data_3.rotate(dif)
    else:
        if data_4[6] != data_3[2]:
            data_4.rotate(dif)
            data_3.rotate(-dif)
            if data_3[6+-dif] != data_2[2]:
                data_2.rotate(dif)
                if data_2[6+dif] != data_1[2]:
                    data_1.rotate(-dif)
        else:
            data_4.rotate(dif)

sum = 0
if data_1[0] == '1':
    sum += 1
if data_2[0] == '1':
    sum += 2
if data_3[0] == '1':
    sum += 4
if data_4[0] == '1':
    sum += 8

print(sum)
