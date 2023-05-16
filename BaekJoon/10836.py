import sys
input = sys.stdin.readline

m,n = map(int,input().split())
up = [1] * (2*m-1)
end = 2 * m-1
for i in range(n):  # 백만
    temp = list(map(int,input().split()))
    for i in range(temp[0], temp[0] + temp[1]): # 최대 1399
        up[i] += 1
    for i in range(temp[0] + temp[1], end):
        up[i] += 2

for i in range(m-1,-1,-1):
    print(up[i],*up[m:])

