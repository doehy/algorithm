import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,v = map(int,input().split())

data = [[]  for i in range(n+1)]

d_visited = [0] *(n+1)
b_visited = [0] *(n+1)

print(d_visited)

for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)


for i in range(n+1):
    data[i].sort()
print(data)

for j in range(n+1):
    for i in data[j]:
        print(i)
        if d_visited[i] == 0:
            d_visited[j] = 1
        





