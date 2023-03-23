def solution(queue1, queue2):
    count = 0
    one_sum = sum(queue1)
    two_sum = sum(queue2)
    total = one_sum + two_sum
    que1 = deque(queue1)
    que2 = deque(queue2)    
    if total % 2 == 1:
        return -1
    while True:
        if one_sum == two_sum:
            return count
        if len(que1) == 0 or len(que2) == 0 or count == (len(que1) + len(que2)) * 2:
            return -1
        count += 1
        if one_sum > two_sum:
            temp = que1.popleft()
            que2.append(temp)
            one_sum -= temp
            two_sum += temp
        else:
            temp = que2.popleft()
            que1.append(temp)
            two_sum -= temp
            one_sum += temp