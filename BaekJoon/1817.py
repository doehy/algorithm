n,m = map(int,input().split())

if n != 0:
    stack = list(map(int,input().split()))

    count = 0
    temp = 0
    i = 0
    flag = 0

    while i < len(stack):
        temp += stack[i] # 새 짐이 생겼어
        if temp <= m: #새 짐의 무게를 새
            if flag == 0: # 상자가 없어
                count += 1 #상자를 만들어
                flag = 1 #만들었따는 신호를줘
        else: #짐이 더 커
            count += 1
            flag = 1
            temp = temp - (temp - stack[i])
        i += 1

    print(count)
else:
    print(0)