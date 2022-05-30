n,s = input().split()

data =[]

for _ in range(int(n)):
    data.append(input().split())

for i in range(len(data)):
    if s == data[i][0]:
        num = i

result = data[num][1]
sum = 0

if num == 0:
    print(0)
else:
    for i in range(num+1):
        if result == data[i][1]:
            sum += 1
    print(sum-1)