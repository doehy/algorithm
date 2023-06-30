from collections import deque
import sys
input = sys.stdin.readline
n,t,w = map(int,input().split()) # n은 오픈전 대기수, t는 한 턴당 상담하는 시간, w는 알아볼 시간
person = deque()
for _ in range(n):
    person.append(list(map(int,input().split())))
openAfterNum = int(input())
oaperson = []
for _ in range(openAfterNum):
    oaperson.append(list(map(int,input().split())))
oaperson = deque(sorted(oaperson, key=lambda x : x[2]))
def solve():
    i = 0
    while i < w: 
        cp = person.popleft()
        if t >= cp[1]: 
            for j in range(cp[1]):
                print(cp[0])
                i += 1
                if i >= w:
                    return
            repeat = 0
            while repeat < len(oaperson):
                if i >= oaperson[repeat][2]:
                    person.append(oaperson.popleft())
                    repeat -= 1
                else:
                    break
                repeat += 1 
        else: 
            for j in range(t):
                print(cp[0])
                i += 1
                if i >= w:
                    return
            cp[1] -= t
            repeat = 0
            while repeat < len(oaperson):
                if i >= oaperson[repeat][2]:
                    person.append(oaperson.popleft())
                    repeat -= 1
                else:
                    break
                repeat += 1        
            person.append(cp)
solve()
