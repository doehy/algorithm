a,b = map(int,input().split())

number = []

count = 0 # 수열은 천개까지 있을 것이다.
num = 0
start = 1

while(count < 1001) :
    num = start
    for _ in range(num):
        number.append(start)
        count += 1
    start += 1

sum = 0

while a <= b:
    sum += number[a-1]
    a += 1

print(sum)
