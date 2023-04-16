import sys
input = sys.stdin.readline

n = int(input())

answer = 0

data = []
mi = 0

for i in range(n):
    x = int(input())    
    data.append(x)
    if x == n:
        mi = i
number = n - 1
count = 1
for i in range(mi,-1,-1):
    if data[i] == number:
        count += 1
        number -= 1

print(n - count)