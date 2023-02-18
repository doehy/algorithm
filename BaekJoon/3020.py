import sys
input = sys.stdin.readline
n,height = map(int,input().split())

floor = []
ceil = []

for i in range(n):
    if i % 2 == 0:
        floor.append(int(input()))
    else:
        ceil.append(int(input()))

floor.sort()
ceil.sort()

def binary_search(arr, h): # index 함수를 이용하여 위치를 찾아내면 간단하지만 시간복잡도 떄문에 굳이 그냥 이분탐색으로 h의 위치를 찾아내는 것
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < h:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1 # end까지 다 부셔버리고 index는 0부터 시작이니 +1을 한다.

min_result = float("inf") 
count = 1
for h in range(1,height+1):
    floor_count = len(floor) - binary_search(floor, h)
    ceil_count = len(ceil) - binary_search(ceil, height-h+1) # ceil은 뒤집어서 생각해야 한다.
    cur_count = floor_count + ceil_count
    if min_result == cur_count:
        count += 1
    elif min_result > cur_count:
        min_result = cur_count
        count = 1

print(min_result,count)



# 게임시작
# 기준점의 후보 : 구간말고는 보이지가 않는데
# 근데 부셔야되는 최소의 개수 그리고 그 구간의 갯수를 구해야하는데 다 알아봐야하는것 아닌가
# 이게 왜 이분탐색이지 이제까지 모든 이분탐색은 기준이 있었는데 이건 기준이 없어 다 탐색해야해
# 일단 floor와 ceil에다가 입력을 받고 재네들을 정렬을 해
