n = int(input())

data = []

for i in range(n):
    if i == 0:
        temp = int(input())
    else:
        data.append(int(input()))

count = 0

if n == 1:
    print(0)
else:
    if max(data) == temp:    
        print(count+1)
    else:
        while temp <= max(data):
            data[data.index(max(data))] -= 1
            temp += 1
            count += 1
        print(count)

