from collections import deque

n = int(input())

data = [[] * n for _ in range(n)]

for i in range(n):
    temp = input()
    for j in range(len(temp)):
        if temp[j:j+1] == 'Y':
            data[i].append(j)

freinds = [0] * n

def check(visited,freinds,num):
    visited[num] = True
    for ppp in data[num]:
        visited[ppp] = True
    freinds[num] = len(data[num])
    q = deque(data[num])
    while q:
        x = q.popleft()
        for k in data[x]:
            if not visited[k]:
                visited[k] = True
                freinds[num] += 1

for uni in range(n):
    visited = [False] * n
    check(visited,freinds,uni)

print(max(freinds))

