import sys
input = sys.stdin.readline

n = int(input())

data = []

for i in range(n):
    data.append(int(input()))

data.sort()

count = 0

for i in range(len(data)):
    count += abs(i+1 - data[i])

print(count)