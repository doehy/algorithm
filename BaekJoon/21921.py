X,N = map(int,input().split())

data = list(map(int,input().split()))

dic = dict()
start = sum(data[:N])
dic[start] = 1 

for i in range(1,X-N+1): # 1부터 3까지 
    start -= data[i-1]
    start += data[i+N-1]
    if start not in dic:
        dic[start] = 1
    else:
        dic[start] += 1

number = max(dic.keys())

if number == 0:
    print("SAD")
else:
    print(number)
    print(dic[number])
