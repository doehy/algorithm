def solution(scores):
    answer = 1
    wangho = scores[0]
    wangho_sum = wangho[0] + wangho[1]
    scores = sorted(scores, key = lambda x : (-x[0], x[1]))
    bf = 0
    for score in scores:
        if score[0] > wangho[0] and score[1] > wangho[1]:
            return -1 
        if bf <= score[1]: # 전에꺼보다만 크거나 같으면 되는 이유는 작으면 x[0]에 대해서 내림차순 했으니 둘다 작아서 인센티브를 못 받고,
            # 그렇게 치면 x[1]에 대해서 오름차순으로 정렬했으니 무조건 크거나 같다고 할 수 있겠지만 x[0]이 달라질 때 조건이 달라진다. 그래서 계속 bf에 값을 넣어주는 것이다.
            if score[0] + score[1] > wangho_sum:
                answer += 1
            bf = score[1]
    return answer
