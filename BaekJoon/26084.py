import sys
input = sys.stdin.readline

def check(d,s):
    temp = 1
    rtemp = 1
    for i in range(s):
        temp *= d
        d -= 1
    tp = s
    for i in range(s):
        rtemp *= tp
        tp -= 1
    return temp // rtemp

s = list(input().rstrip())
n = int(input())
sdata = dict()

for i in range(3):
    if s[i] not in sdata:
        sdata[s[i]] = 1
    else:
        sdata[s[i]] += 1

data = dict()

for i in range(n):
    temp = input()[0]
    if temp in s:
        if temp not in data:
            data[temp] = 1
        else:
            data[temp] += 1

if len(data.keys()) != len(sdata.keys()):
    print(0)
else:
    count = 1
    for i in sdata.keys():
        count *= check(data[i],sdata[i])
        
    print(count)
