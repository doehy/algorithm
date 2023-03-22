from collections import deque

n,k = map(int,input().split())
data = deque(list(map(int,input().split())))

robot = deque([False for i in range(n)])
sum = 0
while True:
    sum += 1
    data.rotate(1)
    robot.rotate(1)
    if robot[n-1] == True: # 내려야하는 위치에 로봇이 있다면
        robot[n-1] = False # 즉시 내려준다.
    for i in range(n-2,-1,-1): #n에서는 그 즉시 내려야하니 n-2부터 확인한다.
        if i == n-2:
            if robot[n-2] == True and data[n-1] >= 1:
                data[n-1] -= 1
                robot[n-2] = False
        else:
            if robot[i] == True: # 
                if data[i+1] > 0 and robot[i+1] == False: 
                    data[i+1] -= 1
                    robot[i] = False
                    robot[i+1] = True
    if data[0] > 0:
        data[0] -= 1
        robot[0] = True
    
    if data.count(0) >= k:
        break
 
print(sum)

