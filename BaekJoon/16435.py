n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

for i in data:
    if m >= i:
        m += 1

print(m)