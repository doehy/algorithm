from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

s = defaultdict(int)

count = 0

for i in data:
    if i not in s or s[i] == 0:
        s[i-1] += 1
        count += 1
    else:
        s[i] -= 1
        s[i-1] += 1
    
print(count)