N,D = map(int,input().split())

data = []

for i in range(N):
    s,e,d  = map(int,input().split())
    if e <= D:
        data.append((s,e,d))

leng = len(data)
result = float("inf")

data = sorted(data, key=lambda x:x[0])

def solve(idx,x,count):
    global result
    if x == D:
        result = min(result,count)
        return
    if idx == leng and x < D:
        result = min(result,count+(D-x))
        return
    if x > data[idx][0]: # 역주행하지 말라는 의미이다.
        solve(idx+1,x,count)
    else:
        if x == data[idx][0]: # 현재 지름길을 탈 수 있는 경우
            solve(idx+1,data[idx][1],count+data[idx][2])
        else: # 현재 지름길을 탈 수 없는 경우
            solve(idx+1,data[idx][1],count+data[idx][2]+(data[idx][0]-x))
        # 이제는 현 지름길을 선택하지 않는 경우이다.
        solve(idx+1,x,count)        

solve(0,0,0)
print(result)
