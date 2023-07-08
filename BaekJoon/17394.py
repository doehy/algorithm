from collections import deque
import sys,math
input = sys.stdin.readline
t = int(input())
dp = [False] * 100001
for i in range(2,int(math.sqrt(100001)) +1):
    if not dp[i]: #소수라면
        for j in range(i*2,100001,i):
            dp[j] = True
            
def cal(n,a,b):
    visited = [0] * (1000001) 
    q = deque()
    q.append(n)
    while q:
        num = q.popleft()
        if a <= num <= b and not dp[num]:
            print(visited[num])
            return
        for i in range(4):
            if i == 0:
                cnum =  num // 3
            elif i == 1:
                cnum = num // 2
            elif i == 2:
                cnum = num - 1
            else:
                cnum = num + 1
            if 0 <= cnum <= 1000000 and not visited[cnum]:
                visited[cnum] = visited[num] + 1
                q.append(cnum)  
    print(-1)

for i in range(t):
    n,a,b = map(int,input().split()) #n을 최대한 나눠보고 a,b에 갈 수 있는지 본다.
    data = [0] * (max(n,b) + 1)
    cal(n,a,b)
