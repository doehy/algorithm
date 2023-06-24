from collections import deque
f,s,g,u,d  = map(int,input().split())
data = [0] * 1000001

q = deque([s])
data[s] = 1
flag = 0
while q:
    floor = q.popleft()
    if floor == g:
        print(data[floor] - 1)
        flag = 1
        break
    temp_data = [floor + u,floor - d]
    for i in range(2):
        if 1 <= temp_data[i] <= f and data[temp_data[i]] == 0:
            data[temp_data[i]] = data[floor] + 1
            q.append(temp_data[i])
if flag == 0:
    print("use the stairs")
        