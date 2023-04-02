def check_deliveries(deliveries, d_idx, cap):
    temp = 0
    tp_idx = 0
    for i in range(d_idx,-1,-1):
        if deliveries[i] > 0:
            tp_idx = max(tp_idx, i)
            if deliveries[i] >= cap - temp:
                deliveries[i] -= cap - temp
                return tp_idx, i
            else: # 자원을 비울 필요가 있나? 그냥 지나가면 되는건데 
                temp += deliveries[i] # 근데 채울 필요는 있지
    return tp_idx, 0

def check_pickups(pickups, p_idx, cap):
    temp = 0
    tp_idx = 0
    for i in range(p_idx,-1,-1):
        if pickups[i] > 0:
            tp_idx = max(tp_idx, i)
            if pickups[i] >= cap - temp:
                pickups[i] -= cap - temp
                return tp_idx, i
            else: # 자원을 비울 필요가 있나? 그냥 지나가면 되는건데 
                temp += pickups[i] # 근데 채울 필요는 있지
    return tp_idx, 0

def solution(cap, n, deliveries, pickups):
    answer = 0
    total_deli = sum(deliveries)
    total_pick = sum(pickups)
    if total_deli == 0 and total_pick == 0:
            return answer
    d_idx, p_idx = n - 1, n - 1 # 마지막부터 간다.
    dist = 0
    while True:
        if total_deli <= 0 and total_pick <= 0:
            return answer
        if deliveries[d_idx] == 0 and d_idx == 0 and p_idx == 0 and pickups[p_idx] == 0:     
            break # sum함수로도 체크할 수 있으나 계산할 때 모든 부분 빼주지 않았기 때문에 안됨
        d_idx, min_d = check_deliveries(deliveries,d_idx,cap)
        p_idx, min_p = check_pickups(pickups,p_idx,cap)
        dist = max(d_idx, p_idx)
        answer += (dist+1) * 2
        d_idx, p_idx = min_d, min_p
        total_deli -= cap
        total_pick -= cap
    return answer