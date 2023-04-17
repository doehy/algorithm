import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

answer = 0
total = sum(data)
sum_s = data[0] + data[1]

for i in range(1,n-1): # 벌벌꿀통 순서인 경우
    answer = max(answer, (total - data[0]-data[i]) + (total - sum_s))
    sum_s += data[i+1]


sum_s = 0
for i in range(1,n-1):
    answer = max(answer, (sum_s+data[i]) + (total-(sum_s+data[0])-data[-1]))
    sum_s += data[i]

sum_s = data[0]
for i in range(1, n-1): # 꿀통벌벌 순서인 경우
    answer = max(answer, (total-data[-1]-data[i]) + (sum_s))
    sum_s += data[i]

print(answer)

# 그리디 알고리즘인데
# 1 직과전으로 보자면
# 꿀벌과 꿀통은 멀리있어야 내가 최대한 꿀을 많이 캘 수 있고
# 꿀벌이 있는 시작지점에 꿀 갯수는 적었으면 좋겠어 어차피 못캐니 손해를 덜기 위해서
# 이게 가장 직관적인 생각인데
# 왜냐하면 최대 십만개이기 ?때문에 조합으로 할라고 하면 무조건 시간초과이다.

# 근데 결국 경우의 수를 구해야하는거 아닌가 흠
# 근데 데이터가 정렬을 시킬 수도 없다.