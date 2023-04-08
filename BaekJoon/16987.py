N = int(input())
data = []
for i in range(N):
    s,w = map(int,input().split())
    data.append([s,w])
answer = 0
def dfs(data,idx,count):
    global answer
    if idx == N: # 든 계란이 가장 오른쪽에 위치할 경우
        answer = max(answer,count)
        return
    if data[idx][0] <= 0: # 든 계란이 이미 깨진 계란이면 오른쪽으로
        dfs(data,idx+1,count)
        return
    # 자신 보다 오른쪽에 있는 계란만 쳐야한다는 말은 없으니까
    egg = True
    for i in range(N):
        if i != idx and data[i][0] > 0: # 자기 자신이 아니면서 깨져있지 않는 계란과 부딪힌다.
            egg = False
            hand = data[idx][1]
            temp = data[i][1]
            data[i][0] -= hand
            data[idx][0] -= temp
            if data[i][0] <= 0 and data[idx][0] <= 0:
                dfs(data,idx+1,count+2)
            elif (data[i][0] <= 0 and data[idx][0] > 0) or (data[i][0] > 0 and data[idx][0] <= 0):
                dfs(data,idx+1,count+1)
            else:
                dfs(data,idx+1,count)
            data[i][0] += hand
            data[idx][0] += temp
    if egg:
        answer = max(answer,count)


dfs(data,0,0)
print(answer)