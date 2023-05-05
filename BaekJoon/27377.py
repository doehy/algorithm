import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    w,cv = int(input())
    count = 1
    answer = w # 일단 처음에는 무조건 써야하니까
    if w < cv: # 일단 w가 cv보다 작은 경우 그리고 이것을 해주는 이유 w가 cv보다 터무니 없이 작아 많은 반복을 하는 것을 피하기 위해서다.
        tp = cv // w
        count += tp
        answer += tp * w # tp와 answer을 즐가시킨다. # 근데 이렇게 하면 n이 2라고 가정하면 n 답이 아니게된다.
    # 그렇다면 처음으로 돌아가서 매번 greedy적이게 선택을 해야하는데 이렇게 하면 또 터무니 없는 반복이 일어날 수도 있다.


#10000
#1000000000000000000

# 보낼 말의 개수가 너무 많아 이건 무조건 그리디로 해야돼
# 최대 만번의 테스트 동안 최대 10의 18승만큼의 보낼 같은말의 갯수가 주어져 하...
