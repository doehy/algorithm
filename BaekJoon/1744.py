import sys
input = sys.stdin.readline
n = int(input())
plus = []
minus = []
zero = 0
result = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero += 1

plus.sort() # 1,2,3
minus.sort(reverse=True) # -20,-50,-100
while len(minus) > 1:
    result += minus[len(minus) - 1] * minus[len(minus) - 2]
    minus.pop()
    minus.pop()
if minus and zero > 0:
    zero -= 1 # 어차피 minus는 pop 해주든 안 해주든 상관이 없으니 걍 안 해줌
elif minus and zero == 0:
    result += minus[0]

while len(plus) > 1:
    if plus[len(plus) - 2] == 1:
        result += plus[len(plus) - 1] + plus[len(plus) - 2]
    else:
        result += plus[len(plus) - 1] * plus[len(plus) - 2]
    plus.pop()
    plus.pop()
if plus:
    result += plus[0]
print(result)




# n의 범위가 50으로 매우 작다. 하지만 모든 경우의 수를 봐야한다. 최댓값을 구해야 한다.
# dp일 가능성이 매우크다. 이건 구현을 어떻게 해야 할까라는 측면에서 봐도 일단 dp이다. 분류를 많이 하면 되지만 좀 귀찮을 것 같다.
# 분류하는 법 일단 음수들은 절댓값이 제일 큰것끼리 곱한다. 남은 것은 0이있으면 곱하고 0이 없으면 양수중 절댓값이 작은 수와 곱한다.
