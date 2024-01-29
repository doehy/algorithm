import sys
input = sys.stdin.readline
n = int(input())
km = list(map(int,input().split()))
money = list(map(int,input().split()))
ans = 0
cur = float("inf")
for i in range(n-1):
    if money[i] < cur:
        cur = money[i]
        ans += cur * km[i]
    else:
        ans += cur * km[i]
print(ans) 



# 백퍼센트 긔리디 도시의 개수가 십만 개 모든 경우의 수를 다 따지면서 구한다 말도 안 된다.
# 일단 다음 도시까지는 무조건 가야되기 떄문에 최소한으로 현재 도시에서는 다음 도시꺼까지는 무조건 충전을 해놔야해
# 이전꺼보다 작은지 확인을 해 오케이 충전을 해 
