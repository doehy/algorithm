n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

graph = []

for c_num,li_num,score in data:
    graph.append([score,c_num,li_num])

graph.sort()
graph.reverse()

result = []
cnt = 0
temp = 0
final_cnt = 0

for score,c_num,li_num in graph:
    if final_cnt == 3:
        break
    if cnt == 1:
        if temp == c_num:
            continue
        else:
            temp = c_num
            final_cnt += 1
            result.append((c_num,li_num))
    else:    
        if temp == c_num:
            cnt = cnt + 1
            final_cnt += 1
            result.append((c_num,li_num))
        else:
            temp = c_num
            final_cnt += 1
            result.append((c_num,li_num))

for x,y in result:
    print(x,y)