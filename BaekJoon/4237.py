import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    answer = 1
    data = list(map(int,input().split()))
    i = 1
    flag = 0
    count = 1
    while i < len(data) - 1:
        if flag == 0: # 깃발이 0은 일단 > 이것
            if data[i] > data[i+1]:
                count += 1
                flag = 1
        else: 
            if data[i] < data[i+1]:
                count += 1
                flag = 0
        i += 1
    answer = max(answer,count)
    print(answer)