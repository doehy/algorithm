N = int(input())

lst = list(map(int,input().split()))

fake = list()

min_num = 1
sum = 0


for i in range(N):
    
    if sum not in fake:
        fake.append(sum)

