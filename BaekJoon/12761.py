from collections import deque

a,b,start,end = map(int,input().split())
data = [float("inf")] * 100001
data[start] = 0
dplus = [b,a,1]

def solve(data):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x * dplus[i]
            if nx <= 100000:
                if data[nx] > data[x] + 1:
                    data[nx] = data[x] + 1
                    q.append(nx)
        for i in range(3):
            nx = x + dplus[i]
            if nx <= 100000:
                if data[nx] > data[x] + 1:
                    data[nx] = data[x] + 1
                    q.append(nx)
        for i in range(3):
            nx = abs(x - dplus[i])
            if 0 <= nx:
                if data[nx] > data[x] + 1:
                    data[nx] = data[x] + 1
                    q.append(nx)

solve(data)
print(data[end])
# 방문을  했다해서 최소가 아니였을 수 도 있기에 방문을 안하면 안되고
# 방문한것을 또 방문 가능하게 하면 무한하게 돼서 흠...
# 작다면 곱하고 더하고 +1 
# 크다면 나누고 빼고 -1
# 근데 20이 되면 더 이상 큐 들어갈 필요가 없지
# +1 -1이 있기 때문에 어ㄸ허게든 20으로 가지만 아 근데 십만에서는 내려오지 않겠구만
# 커진 순간 마이너스 a,b를 해서 내려올 거니까
