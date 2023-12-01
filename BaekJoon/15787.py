import sys
input = sys.stdin.readline
n,m = map(int,input().split())

data = [0] * (20*n)

for i in range(m):
    text = input().split()
    if text[0] == '1':
        data[(int(text[1])-1)*20+(int(text[2])-1)] = 1
    elif text[0] == '2':
        data[(int(text[1])-1)*20+(int(text[2])-1)] = 0
    elif text[0] == '3':
        for i in range(int(text[1])*20-1,(int(text[1])-1)*20-1,-1):
            if i-1 >= (int(text[1])-1)*20:
                data[i] = data[i-1]
        data[i] = 0                  
    elif text[0] == '4':
        for i in range((int(text[1])-1)*20+1,int(text[1])*20):
                data[i-1] = data[i]
        data[i] = 0

result = 0
temp_data = []

for i in range(n):
    flag = 0
    if i == 0:
        temp_data = data[:20]
        result += 1
        continue
    else:
        for j in range(1,len(temp_data)//20+1):
            if temp_data[(j-1)*20:j*20] == data[i*20:(i+1)*20]:
                flag = 1
                break
        if flag == 0:
            temp_data.extend(data[i*20:(i+1)*20])
            result += 1

print(result)
    
    

