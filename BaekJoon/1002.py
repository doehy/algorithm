import sys, math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dis = math.sqrt((x1-x2)**2 + (y1-y2) **2)

    if dis == 0: # 중심이 같아
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else: # 중심이 달라
        if r1+r2 < dis: # 외부에 위치해
            print(0)
        elif r1 + r2 == dis: # 외접해
            print(1)
        elif r1 + r2 > dis: # 일단 원 하나가 원 하나랑 겹쳐
            if abs(r1-r2) == dis: # 내접이야
                print(1)
            elif abs(r1-r2) > dis: # 안에 그냥 쏙 들어왔어
                print(0)
            else:
                print(2)