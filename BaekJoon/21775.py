from collections import deque
import sys
input = sys.stdin.readline

n,t = map(int,input().split())
data = list(map(int,input().split()))
cards = deque() 
private = set() # 사적인 공간에 있냐 없냐
visited = [0] * (n+1) # 연산 카드를 들고 있냐
ps = [[] for _ in range(n+1)] # 어떤 연산 카드를 들고 있냐
for _ in range(t):
    card = input().split() # 일단 이렇게 입력받아야해
    cards.append(card)

def solve():
    i = 0
    while i < t: # 턴 안 동안
        if visited[data[i]] == 0: # 연산카드를 들고 있지 않다면 카드 하나를 꺼낸다.
            card = cards.popleft()
            visited[data[i]] = 1
            if card[1] == 'next': 
                print(card[0])
                visited[data[i]] = 0
            elif card[1] == 'acquire': # 카드 하나를 꺼낸게 이거였다면
                if card[2] not in private: # 사적인 공간에 없다면
                    visited[data[i]] = 0 # 카드 반납하고
                    private.add(card[2]) # 카드를 사적인 공간에 추가한다.
                    print(card[0])
                else: # 사적인 공간에 있으면 가져오지 못하니까
                    ps[data[i]].append(card) #연산 카드를 저장한다.
                    print(card[0]) # 일단 이번 턴에 이 카드를 들고 있던 거니까 출력하고
            else: #획득하지 않는 자원을 release하는 경우는 없으니
                visited[data[i]] = 0 #바로 반납한다.
                private.discard(card[2]) # 공용 공간에 카드를 반납한다.
                print(card[0]) # 들고 있던 연산 카드 id 카드 출력
        else: #연산카드를 들고 있었다는 것은 acquire일 때 밖에 없다.
            if ps[data[i]][0][2] not in private: # 사적인 공간에 없다면
                visited[data[i]] = 0 # 연산 카드 반납
                private.add(ps[data[i]][0][2]) # 카드를 사적인 공간에 추가한다.
                print(ps[data[i]][0][0])
                ps[data[i]].pop()
            else: 
                print(ps[data[i]][0][0])
        i += 1

solve()