import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = list(map(int,input().split()))
data.sort(reverse=True)
min_num = 0
max_num = max(data)
temp = 0
while min_num <= max_num:
    medium_num = (min_num + max_num) // 2
    sum = 0
    flag = 0
    for i in range(len(data)):
        if medium_num < data[i]:
            sum += (data[i] - medium_num)        
            if sum > m:
                temp = medium_num
                min_num = medium_num +1
                break
    if sum == m:
        print(medium_num)
        flag = 1
        break
    if sum < m:
        max_num = medium_num -1

if flag == 0:
    print(temp)


