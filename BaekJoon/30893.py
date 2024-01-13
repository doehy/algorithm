from collections import deque
import sys
input = sys.stdin.readline
n,s,e = map(int,input().split())
data = [[] for _ in range(n+1)]
for i in range(n-1):
    x,y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)

def solve(s,e):
    visited = [0] * (n+1)
    visited[s] = 1
    q = deque()
    q.append([s,0,"s"])
    while q:
        x,dep,who = q.popleft() 
        if len(data[x]) > 2 and who == 'f':  
            return 0
        else:
            if who == 's':
                for next in data[x]:
                    if next == e: # 도착했으면 1리턴해야지
                        return 1
                    if not visited[next]:
                        visited[next] = 1
                        q.append([next, dep+1,"f"])
            else:
                for next in data[x]:
                    if not visited[next]:
                        visited[next] = 1
                        q.append([next, dep+1,"s"])
    return 1

if solve(s,e):
    print("First")
else:
    print("Second")