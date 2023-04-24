n = int(input())
answer = 0
count = 1
while n > 0:
    if n < count:
        count = 1
    n -= count
    answer += 1
    count += 1

print(answer)