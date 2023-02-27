from itertools import combinations

N, L, R, X = map(int,input().split())

data = list(map(int,input().split()))

result = 0
def solve(li):
    left,right = min(li), max(li)
    total = sum(li)
    if L <= total <= R and (right - left) >= X: 
        return 1
    return 0
for i in range(2,len(data)+1):
    for li in combinations(data,i):
        result += solve(li)
print(result)
# 모든 경우를 다 탐색해야하는데 시간 제한이 2초이고 n도 최대 15이니 완전탐색을 해도 될 것 같지만 뭔가 시간초과가 날 것 같다.
# 이분탐색은 죽어도 아니고 그리디도 아니고 끽 해봐야 dp도 아님 저장이 안됨
# 알고리즘은 일단 맞았고 가보자
