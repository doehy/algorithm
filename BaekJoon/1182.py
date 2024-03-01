from itertools import combinations
import sys
input = sys.stdin.readline
n,s = map(int,input().split())
data = list(map(int,input().split()))
result = 0
for i in range(1,n+1):
    for j in combinations(data,i):
        if sum(j) == s:
            result += 1
print(result)
