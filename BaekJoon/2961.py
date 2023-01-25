from itertools import combinations

n = int(input())

data = []

for i in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

def cal(li):
    sin = 1
    ssun = 0
    for a,b in li:
        sin *= a
        ssun += b
    return abs(sin - ssun)

result = float("inf")

for i in range(1,n+1):
    for li in combinations(data,i):
        result = min(result,cal(li))

print(result)
# 경우의 수를 다 따져봐야 한다.
# 조합적으로 접근하면 괜찮을 것 같다. 재료가 최대 10개이다.
