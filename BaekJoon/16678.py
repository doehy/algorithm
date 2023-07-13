import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    honor = int(input())
    data.append(honor)
answer = []
num = 1
idx = 0
result = 0
data.sort()
while idx < len(data):
    if num != data[idx]:
        if data[idx] >= num:
            result += data[idx] - num
            num += 1
        else:
            pass
    else:
        num += 1
    idx += 1
print(result)