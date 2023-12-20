import sys
input = sys.stdin.readline

n = int(input().rstrip())

data = dict()

for i in range(n):
    s = input().rstrip().split('.')
    if s[1] not in data:
        data[s[1]] = 1
    else:
        data[s[1]] += 1

result = sorted(data.items())
for i in result:
    print(*i)