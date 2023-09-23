import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
maxNumber = max(data)
numbers = [-1] * (maxNumber+1)   
result = [0] * n
for i in range(n):
    numbers[data[i]] = i

for i in data:
    for j in range(i+i, maxNumber+1, i):
        if numbers[j] > -1:
            result[numbers[i]] += 1
            result[numbers[j]] -= 1

print(*result)