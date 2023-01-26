import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    day = int(input())
    data = list(map(int,input().split()))
    result = 0
    temp = data[-1]
    count = 0
    total = 0
    for j in range(day-2,-1,-1):
        if data[j] > temp:
            result += temp * count - total
            count = 0
            total = 0
            temp = data[j]
        else:
            count += 1
            total += data[j]
    if count > 0:
        result += temp * count - total
    print(result)


