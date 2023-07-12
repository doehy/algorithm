import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
ans = float("inf")
l,r = 0, len(data) - 1
flag = 0
while l < r: # 여기서는 용액 두개를 합치는 것이기 때문에 같아지면 의미가 없다.
    tp = data[r] + data[l]
    if tp == 0:
        flag = 1
        break
    elif tp > 0:
        r -= 1
    else:
        l += 1
    if abs(ans) > abs(tp):
        ans = tp
if flag == 1:
    print(0)
else:
    print(ans)
# 투포인터의 도달하는 과정
# 조합을 쓰기에는 시간이 너무 오래 걸려 그렇다면 나머지는 투 포인터야 
# 포인터 위치를 어느 기준으로 조정해야할까가 문제인데
# 0에 가까워져야 하니 0을 기준으로 설정해 만약 0보다 더 큰데 r을 냅두고 l을 늘려버리면 오히려 0에서 더 멀어지기 때문에 0을 키워야 한다.