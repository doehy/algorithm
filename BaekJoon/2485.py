import sys
input = sys.stdin.readline
n = int(input())
tree = [int(input())]
dif = []
result = 0
for _ in range(n-1):
    tree.append(int(input()))
    dif.append(tree[-1] - tree[-2])

def makeGreatDivisor(x1, x2):
    if x1 % x2 != 0:
        return makeGreatDivisor(x2, x1 % x2)
    else:
        return x2
first = makeGreatDivisor(dif[0],dif[1])
for i in range(2,len(dif)):
    first = min(first, makeGreatDivisor(first, dif[i]))
for i in range(n-1):
    result += (tree[i+1] - tree[i]) // first - 1
print(result)
