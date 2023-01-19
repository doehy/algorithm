from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    temp = deque([tree.pop()])
    min_result = 0
    right_num = tree.pop()
    min_result = max(min_result,abs(temp[-1] - right_num))
    left_num = tree.pop()
    min_result = max(min_result,abs(temp[-1] - left_num))
    flag = 0
    while tree:
        if flag == 0:    
            temp = tree.pop()
            min_result = max(min_result,abs(right_num - temp))
            right_num = temp
            flag = 1
        elif flag == 1:
            temp = tree.pop()
            min_result = max(min_result,abs(left_num - temp))
            left_num = temp
            flag = 0
    min_result = max(min_result,abs(right_num - left_num))
    print(min_result)