n = int(input())
leng = int(input())
data = [[] for _ in range(n+1)]

for i in range(leng):
    x,y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)

result = {1}
for i in data[1]:
    result.add(i)

for i in data[1]:
    for j in data[i]:
        if j not in result:
            result.add(j)

print(len(result)-1)