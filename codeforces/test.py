n = int(input())

for i in range(n):
    x,k = map(int,input().split())
    count = 0
    answer = []
    tx = x # 10
    while x != 0: # 10
        if tx % k != 0: # 10 2 9 2
            x -= tx # 1
            answer.append(tx)
            tx = x # 1
            count += 1
        else:
            tx -= 1
    print(count)
    print(*answer)
