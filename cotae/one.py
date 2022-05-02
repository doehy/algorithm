N,M = map(int,input().split())

num = 0

while N != 1:
    if N % M == 0:
        N /= M
        num += 1
    else:
        N -= 1
        num += 1
print(num)
