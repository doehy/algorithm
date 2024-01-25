import sys
input = sys.stdin.readline

n = int(input())
bead = []
for _ in range(n):
    bead.append(int(input()))

maxNum = max(bead)
sumNum = sum(bead)

if maxNum > sumNum - maxNum:
    print(maxNum - (sumNum - maxNum))
else:
    print(1 if sumNum % 2 else 0)