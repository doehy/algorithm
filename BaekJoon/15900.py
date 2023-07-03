import sys
input = sys.stdin.readline
n = int(input())
data = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

count = 0

visited = [False] * (n+1)
stack = [(1,0)]

while stack:
    node, cnt = stack.pop()
    visited[node] = True
    if len(data[node]) == 1 and node != 1:
        count += cnt
        continue

    for i in data[node]:
        if visited[i] == False:
            stack.append((i,cnt+1))

print(count)

if count % 2 == 0:
    print("No")
else:
    print("Yes")