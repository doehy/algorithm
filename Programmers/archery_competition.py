from collections import deque
def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        target, arrow = q.popleft()

        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if lion > apeach:
                gap = lion - apeach
                if gap > maxGap:
                    maxGap = gap
                    res.clear()
                    res.append(arrow) # 흠 이렇게 하면 되는 것 아닌가
                if gap == maxGap:
                    res.append(arrow)
        elif sum(arrow) > n: # 화살을 많이 쐈다면
            continue
        elif target == 10: # 마지막 좌표를 가리키는데 화살을 덜 쐈어 그렇다면 마지막 좌표에다가 다 쏜다. 
            tmp = arrow.copy()
            tmp[target] = n - sum(tmp)
            q.append((-1, tmp))
        else:
            tmp = arrow.copy()
            tmp[target] = info[target] + 1
            q.append((target+1, tmp))
            tmp2 = arrow.copy()
            tmp2[target] = 0
            q.append((target+1, tmp2))
    return res

def solution(n, info):
    answer = bfs(n, info)
    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    else:
        return answer[-1]
