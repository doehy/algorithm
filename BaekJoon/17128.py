n,q = map(int,input().split())

data = list(map(int,input().split()))

hihi = list(map(int,input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = data[i] * data[i-1] * data[i-2] * data[i-3] # 슬라이싱에는 마이너스가 존재한다. 까먹지말자

result = sum(dp)

for idx in hihi:
    for i in range(4):
        new_idx = (idx-1+i) % n
        dp[new_idx] = -dp[new_idx]
        result += 2 * dp[new_idx]
    print(result)