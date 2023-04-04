from collections import deque
import sys
input = sys.stdin.readline
number = int(input())
data = [[] for i in range(number+1)]
while True:
    x,y = map(int,input().split())
    if x == -1 and y == -1:
        break
    data[x].append(y)
    data[y].append(x)

info = dict()

def find(num,visited):
    q = deque()
    q.append(num)
    visited[num] = 1
    while q:
        x = q.popleft()
        for i in data[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return max(visited) - 1
# 아 둘이 직접적인 친구가 아닌 경우에만 어떤 거리로 친구인지만 구하면 된다.

for i in range(1,number+1):
    visited = [0] * (number + 1)
    cnt = find(i,visited)
    if cnt not in info:
        info[cnt] = [i]
    else:
        info[cnt].append(i)

min_num = min(info.keys())
print(min_num, len(info[min_num]))
print(*list(info[min_num]))
