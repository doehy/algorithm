import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
result = 0
data.sort(reverse=True)
leng = []
i = 0
while i < n-1:
    if data[i] - data[i+1] == 0:
        leng.append(data[i])
        i += 2
    elif data[i] - data[i+1] == 1:
        leng.append(data[i+1])
        i += 2
    else:
        i += 1

if len(leng) % 2 == 0:
    for i in range(0,len(leng),2):
        result += leng[i] * leng[i+1]
else:
    for i in range(0,len(leng)-1,2):
        result += leng[i] * leng[i+1]
print(result)
