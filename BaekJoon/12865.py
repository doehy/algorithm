N,K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)] # 굳이 1씩 증가시킬 필요없다고 생각하지만 나중에 배열 index를 위해서 고려해주자
data = [[0,0]]

for _ in range(N):
    W,V = map(int,input().split())
    data.append([W,V])

data = sorted(data, key=lambda x : x[0])

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= data[i][0]: # 맥스 한계치가 현재 소지품의 무게보다 크거나 같다면 현재 소지품이 들어가는 경우
            # 이 물건을 넣기 위해 공간을 확보하는 경우와, 확보해서 넣어도 무게만 차지하고 가치는 낮을 수도 있기에 이 무게였을 때의 최댓값 비교
            # 현재 i 인덱스에서는 j의 무게가 아직 안 정해졌으니 
            dp[i][j] = max(dp[i-1][j - data[i][0]] + data[i][1],dp[i-1][j])
        else: # 맥스 한계치가 현재 소지품의 무게보다 작다면 
            dp[i][j] = dp[i-1][j] # 이 무게에서 이 소지품이 담기기 전이었을때의 최대 무게

print(dp[N][K])

# 헷갈렸던 부분 마지막에 무게는 낮은데 가치가 엄청 높은 보석이 있으면 어떡하지 고려가 안되는 것 아닌가
# 16행 dp[i-1][j - data[i][0]] 여기서 고려가 된다.