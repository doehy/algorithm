n,k = map(int,input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))

result = 0

coin.reverse()

cnt = 0
for i in coin:
    if i > k :
        continue 
    else: # i <- k라는 말 목표금액이 크거나 같다는 말
        cnt = k // i
        k = k - i*cnt
        result += cnt
        cnt = 0

print(result) 


