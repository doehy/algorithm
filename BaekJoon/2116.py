n = int(input())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

dx = [[0,5],[1,3],[2,4]]
count = 0
for i in range(6): # 첫 주사위에 윗면이 위를 향하는 숫자의 인덱스
    temp = 0    
    up_idx = i
    down_idx = 0
    
    for x,y in dx:
        if up_idx == x or up_idx == y:
            down_idx = (x+y) - up_idx
            break
    if 6 not in [data[0][up_idx],data[0][down_idx]]:
        temp += 6
    elif 5 not in [data[0][up_idx],data[0][down_idx]]:
        temp += 5
    elif 4 not in [data[0][up_idx],data[0][down_idx]]:
        temp += 4
    for j in range(1,n): # 두 번재 주사위부터 끝까지
        down_idx = data[j].index(data[j-1][up_idx])
        for x,y in dx:
            if down_idx == x or down_idx == y:
                up_idx = (x+y) - down_idx
                break
        if 6 not in [data[j][up_idx],data[j][down_idx]]:
            temp += 6
        elif 5 not in [data[j][up_idx],data[j][down_idx]]:
            temp += 5
        else:
            temp += 4
    count = max(count, temp)
print(count)