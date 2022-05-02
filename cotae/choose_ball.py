n,m = map(int,input().split())

data = list(map(int,input().split()))
array = [0] * 11

result = 0 # 결과 값이다.
number = 0

for x in data:
    array[x] += 1

for i in range(1,m+1):
    n -= array[i]
    result += array[i] * n

print(result)