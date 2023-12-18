import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
temp = dict()
temp = defaultdict(int)
for i in range(n):
    req = list(map(int,input().split()))
    if req[0] == 1:
        temp[req[2]]=(req[1])
    else:
        print(temp[req[1]])
