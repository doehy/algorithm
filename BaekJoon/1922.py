n = int(input())
m = int(input())

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


graph = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    graph.append((cost,a,b))

parent = [0] * (n+1) # 부모 노드를 만든다.

#부모테이블을 초기화 시킨다.
for i in range(1,(n+1)):
    parent[i] = i

result = 0

graph.sort()

for cost,a,b in graph:
    if find(a) != find(b):
        result += cost
        union(a,b)

print(result)

 