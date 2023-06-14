import sys
n,m = map(int,input().split())
data = list(map(int,input().split()))
coverDay = sum(data) + len(data)
notCoverDay = m - coverDay
data = []
if m <= 0:
    print(0)
else:
    answer = 0
    onePlusDay = notCoverDay % (n+1)
    data += [notCoverDay // (n + 1)] * ((n+1) - onePlusDay)
    data += [notCoverDay // (n + 1) + 1] * (onePlusDay)
    for i in data:
        for j in range(1,i+1):
            answer += j ** 2
    print(answer)
# 게임시작
# data에서 행복도를 하나씩 꺼낸다
# 행복이 0이 될때까지 날짜를 넘긴다
# 더 이상의 행복이 남아있지 않다면 남은 날짜를 제곱해서 answer에 더한다음 끝낸다. 근데 이렇게 하면 안 돼 우울이 너무 커져
# 그렇다면 어차피 커버할 수 있는 날은 정해져있어
# 약속 개수와 커버할 날이 같다면 그건 그냥 커버할 날만큼만 출력하면 돼
# 근데 커진 순간 그걸 최대한 작은 숫자들로 쪼개야해