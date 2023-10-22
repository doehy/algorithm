T = int(input())

def binary_search(j):
    if j == 1:
        return 0
    left, right = 0, len(B) - 1
    while left <= right:
        mid = (left + right) // 2
        if B[mid] < j:
            left = mid + 1
        else:
            right = mid - 1
    return left

for i in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    # T 크기가 안 주어진 멍청한 문제다. n,m이 최대 이만의 크기를 가진다.
    # 최악의 경우 완전 탐색일 시 최대 4억이 돼서 시간초과가 나온다.
    # 각 숫자마다 이분탐색을 갈기면 되긴 하는데 이게 맞는 것 같다.
    A.sort(reverse=True)
    B.sort()
    result = 0
    for j in A:
        cnt = binary_search(j)    
        if cnt == 0:
            break
        result += cnt
    print(result)