import sys
input = sys.stdin.readline
n,c = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

def binary_search(left,right,diff):
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == diff:
            return 1
        elif data[mid] > diff:
            right = mid - 1
        else:
            left = mid + 1
    return 0

def check(n,c):
    if c in data:
        return 1
    i, j = 0, n-1
    while i < j:
        total = data[i] + data[j]
        if total > c:
            j -= 1
        elif total == c:
            return True
        else:
            diff = c - total
            if data[i] != diff and data[j] != diff and binary_search(i,j,diff):
                return True
            i += 1
          
if check(n,c):
    print(1)
else:
    print(0)