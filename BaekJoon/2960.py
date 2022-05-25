n,k = map(int,input().split())

data = []

for i in range(2,n+1):
    data.append(i)

num = 0

flag = 0

while True:
    temp = min(data)
    for x in data:
        if x % temp == 0:
            num += 1
            if num == k:
                print(x)
                flag = 1
                break
            data.remove(x)
    if flag == 1:
        break            
                