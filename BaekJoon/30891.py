import sys
input = sys.stdin.readline
n,r = map(int,input().split())
data = []
maxCount = 0
rx,ry = 200,200
for _ in range(n):
    x,y = map(int,input().split())
    data.append([x,y])

for i in range(-100,101):
    for j in range(-100,101):
        count = 0
        for x,y in data:
            if (i-x) ** 2 + (j-y) ** 2 <= r ** 2:
                count += 1
        if maxCount < count:
            maxCount = count
            rx,ry = i,j

print(rx,ry)
