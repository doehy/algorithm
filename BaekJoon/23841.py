n,m = map(int,input().split())

data = []
for i in range(n):
    data.append(list(input()))

for i in range(n):
    for j in range(m):
        if data[i][(m-1)-j] == '.':
            data[i][(m-1)-j] = data[i][j]

for i in data:
    print(''.join(i))