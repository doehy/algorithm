from itertools import permutations

def check(x, y, z, cnt):
    global answer
    if x <= 0 and y <= 0 and z <= 0: # 체력이 0,0,0 됐으면 초기화 시켜야지
        if answer > cnt:
            answer = cnt
            return
    
    x = 0 if x < 0 else x
    y = 0 if y < 0 else y 
    z = 0 if z < 0 else z

    if data[x][y][z] <= cnt: # cnt가 더 크다면 밑으로 내려갈 필요가 없다 내려가 봤자 숫자는 더 늘어나고 의미없는 반복만 늘어난다.
        return
    
    data[x][y][z] = cnt # 이 체력까지는 cnt만에 올 수 있다.

    for i in permutations([9,3,1], 3):
        check(x - i[0], y - i[1], z - i[2], cnt + 1)
        
n = int(input())
scv = list(map(int,input().split()))
while len(scv) < 3:
    scv.append(0)
answer = 30
data = [[[30] * 61 for i in range(61)] for j in range(61)]
check(scv[0], scv[1], scv[2], 0)
print(answer)   