N, K = map(int,input().split())

data = list(map(int,input().split()))

start_leng = [0,data[0]]

temp = data[0]

for i in range(1,len(data)):
    temp += data[i]
    start_leng.append(temp)

temp = start_leng[-1]

for i in range(len(data)-1,-1,-1):
    temp += data[i]
    start_leng.append(temp)

if K == 0:
    print(1)
else:
    for i in range(len(start_leng) - 1):
        if start_leng[i] <= K < start_leng[i+1]:
            if i < N:
                print(i+1)
            else:
                print(N-(i-N))
            break

