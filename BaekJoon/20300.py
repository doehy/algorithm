n = int(input())
data = list(map(int,input().split()))

data.sort() # 데이터를 오름차순으로 정렬한다.
start, end = data[0]+data[1], data[-1]+data[-2]
maxdata = 0

if n % 2 == 0:
    for i in range(0,n//2):
        maxdata = max(maxdata,data[i]+data[n-1-i])
    print(maxdata)
else:
    for i in range(0,n//2):
        maxdata = max(maxdata,data[i]+data[n-2-i])
    if maxdata > data[-1]:
        print(maxdata)
    else:
        print(data[-1])
        