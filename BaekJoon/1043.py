import sys
input = sys.stdin.readline
n,m = map(int,input().split())
knowTruth = list(map(int,input().split()))[1:]
parent = list(range(n+1))
parties= []

def find(node):
    if node != parent[node]: 
        parent[node] = find(parent[node]) 
    return parent[node]

def union(a,b):
    a = find(a)
    b = find(b)

    if a in knowTruth and b in knowTruth: #둘다 진실을 아는 사람이면 트리를 맺어줄 필요가 없다.
        return 
    
    if a in knowTruth:
        parent[b] = a

    elif b in knowTruth:
        parent[a] = b
    
    else: #둘 다 진실을 모른다면 작은 숫자가 부모가 되게 만들어 준다.
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


for i in range(m):
    partyInfo = list(map(int,input().split()))
    partyLen = partyInfo[0]
    party = partyInfo[1:]

    for i in range(partyLen-1):
        union(party[i], party[i+1])

    parties.append(party)

ans = 0

for party in parties:
    flag = 0
    for i in range(len(party)):
        if find(party[i]) in knowTruth:
            flag = 1
            break
    if flag != 1:
        ans += 1

print(ans)