import math

n,l = map(int,input().split())

data = list()
for i in range(n):
    x,y = map(int,input().split())
    data.append((x,y))

data = sorted(data, key=lambda x : x[0])

result = 0
temp = 0

for x,y in data:
    if temp > x:
        x = temp
    print(temp,x,y)
    cnt = math.ceil((y - x) / l)
    temp = x + cnt * l
    result += cnt

print(result)
     