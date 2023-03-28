# 특정 원소가 속한 집합을 찾기
# def find(x):
#     if parent[x] != x:
#         return find(parent[x])
#     return x

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 바꾸기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Unio 연산)의 개수 입력 받기
v, e, money= map(int,input().split())
parent = [0] * (v+1) # 부모 테이블을 만든다.
data = list(map(int, input().split()))

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union(a,b)

result = dict()

for k in range(1, v+1):
    i = find(k)
    if parent[i] not in result:
        result[parent[i]] = data[k-1]
    else:
        if data[k-1] < result[parent[i]]:
            result[parent[i]] = data[k-1]

total = sum(result.values())

if money >= total:
    print(total)
else:
    print("Oh no")

# 유니온 파인드로 각각 부모를 다 찾아놨는데 갱신이 덜 된 애들이 있다.
