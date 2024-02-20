import sys
input = sys.stdin.readline
n,q = map(int,input().split())
square = list(map(int,input().split()))

def solve(x,y):
    ans = 0
    rightCount = square[y-1] - (x-1)
    if rightCount > 0:
        ans += rightCount
    else:
        return 0
    left, right = 0, len(square) - 1
    temp = 0
    while left <= right:
        mid = (left + right) // 2
        if square[mid] >= x:
            temp = mid
            left =  mid + 1
        else:
            right = mid - 1
    ans += (temp + 1) - y
    return ans

for _ in range(q):
    x,y = map(int,input().split())
    print(solve(x,y))


# 세로의 길이는 최대 이십오만, 레이저의 개수는 최대 이십오만

