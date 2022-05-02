N,M,K = map(int,input().split())

coin_type = list(map(int,input().split()))

num_limit = 0
max = 0
max_temp = 0
sum = 0

while True:
    for coin in coin_type:
        if coin > max:
            max = coin
            max_temp = max
    for i in range(K):
        sum += max
        num_limit += 1
        if i == K-1:
            coin_type.remove(max) 
            max = 0   
            for coin in coin_type:
                if coin > max:
                    max = coin
            sum += max
            num_limit += 1
    if num_limit == M:
        break
    else:
        coin_type.append(max_temp)

print(sum)


    