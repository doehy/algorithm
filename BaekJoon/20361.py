n,x,k = map(int,input().split())

data = []

for i in range(n):
    data.append(i+1)

info = []

for i in range(k):
    info.append(list(map(int,input().split())))

for p,q in info:
    data[p-1],data[q-1] = data[q-1],data[p-1]

print(data.index(x)+1)