import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

for k in data:
    print(k)
