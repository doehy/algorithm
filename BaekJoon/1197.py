v,e = map(int,input().split())

def find(a): #부모의 부모를 찾아간다.
    if parent[a] != a: #여기서 노드번호와 노드값이 다를경우라고 조건문을 만든 이유는
        parent[a] = find(parent[a])#부모노드를 찾아서 리스트에 넣어놨고 자신이 최고 조상이면 리스트에는 자신 번호가 들어가 있을 것이고 그래야 재귀함수를 탈출 할 수 있다.
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i
#부모노드들을 일단 자기 자신으로 초기화를 해놓는다.

graph = []

#간선]의 개수 만큼 입력 받아 노드들을 연결해 줄 것이다.

for _ in range(e):
    a,b,cost = map(int,input().split())
    graph.append((cost,a,b))

# 비용을 기준으로 오름차순 정렬할 것이기 때문에 
# 위에서 cost를 먼저 받은 것이다.
graph.sort()

sum = 0
#간선의 개수만큼 해볼 것이다.
for cost,a,b in graph:
    if find(a) != find(b):
        sum += cost
        union(a,b)
     #부모가 같을 경우는 그냥 패스해도 될 것 같다.

print(sum)


