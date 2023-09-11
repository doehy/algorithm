import sys
aCnt, oCnt = map(int,input().split())
aTime = list(map(int,input().split()))
bTime = list(map(int,input().split()))
a = o = 1
aTime.sort()
bTime.sort()
aTemp = [aTime[0]]
bTemp = [bTime[0]]
for i in range(1, len(aTime)):
    if aTime[i] - aTemp[-1] >= 100:
        aTemp.append(aTime[i])
        a += 1
for i in range(1, len(bTime)):
    if bTime[i] - bTemp[-1] >= 360:
        bTemp.append(bTime[i])
        o += 1

print(a, o)
