n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort(reverse = True)

temp = [[0] * 1 for i in range(m)]

number = 0
max_num = 0
for i in range(n):
    if temp[number][0] + data[i] >= max_num:
        max_num =  temp[number][0] + data[i]
        temp[number][0] += data[i]
        if number == m - 1:
            number = 0
        else:
            number += 1
    else:
        temp[number][0] += data[i]
        
print(max(map(max,temp)))
