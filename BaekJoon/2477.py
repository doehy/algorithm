k = int(input())

data = []

for _ in range(6):
    data.append(list(map(int,input().split())))

max_result = 0
max_hi = 0
sum = 0

for i in range(6):
    temp = data[i][0]
    if temp == 3 or temp == 4:
        num = data[i][1]
        max_result = max(num,max_result)
    elif temp == 1 or temp ==2:
        num = data[i][1]
        max_hi = max(num,max_hi)

if data[2][0] == 4: 
    if data[3][0] == 2:
        if data[4][0] == 4:
            sum = data[3][1] * data[4][1]
        else:
            sum = data[4][1] * data[5][1]
    else:
        sum = data[2][1] * data[3][1]
else:
    sum = data[1][1] * data[2][1]

print((max_result * max_hi - sum)*k)