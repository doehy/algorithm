n , w, l = map(int,input().split())

data = list(map(int,input().split()))

# 일단 트럭을 싣기 전에 최대하중이 넘어가는지 안넘어가는지 확인
# 넘어간다면 기다리고 트러들을 보내
# 안넘어간다면 실어
# 마지막이 다 건널때까지 기다려
# 그리고 출력

result = 0

truck = list() #다리위에있는 트럭들
tr_c = 0 # 다리위 트럭들의 무게

for i in data:
    tr_c += i
    if tr_c <= l:
        if truck:
            temp = 0
            for k in range(len(truck)):
                truck[k-temp][0] -= 1
                if truck[k-temp][0] == 0:
                    tr_c -= truck[k-temp][1]
                    truck.remove(truck[k-temp])
                    temp += 1
        truck.append([w,i])
        result += 1
    else:
        while tr_c > l: #그리고 최대하중보다 작아질때까지 기다린다.
            temp = 0
            result += 1
            for j in range(len(truck)):
                truck[j-temp][0] -= 1
                if truck[j-temp][0] == 0: #다리를 다 건넌거니
                    tr_c -= truck[j-temp][1]
                    truck.remove(truck[j-temp])
                    temp += 1
        truck.append([w,i])

if truck:
    result += (truck[len(truck)-1][0])
    print(result)
else:
    print(result)
                     
            


