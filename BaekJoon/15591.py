from collections import deque
import sys
input = sys.stdin.readline
n,question = map(int,input().split())
data = [[] for _ in range(n+1)]
answer = [[] for _ in range(n+1)]
for _ in range(n-1):
    p,q,r = map(int,input().split())
    data[p].append([q,r])

q = deque()
q.append([1,float("inf")])
while q:
    node, usado = q.popleft()
    for next, nextUsado in data[node]:
        number = min(usado, nextUsado)
        answer[node].append([next, number])
        answer[next].append([node, number])
        q.append([next,number])

print(answer)
for _ in range(question):
    k,v = map(int,input().split())





# 게임 시작
# 알고리즘 분류를 먼저 봤어 알고리즘에서 너비 우선 탐색이래 왜 그렇다면 너비 우선 탐색일까
# 너비 우선 탐색은 가까이 있는 것부텀 먼저 탐색하는 것이 너비 우선 탐색이야
# 첫째 입력이 크기 때문에 깊이 우선탐색은 하면 안돼 
# 둘째 