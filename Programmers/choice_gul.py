def solution(k, tangerine):
    answer = 0
    temp = list(set(tangerine))
    tangerine.sort()
    temp.sort()
    tp = []
    num = 0
    for i in range(len(temp)-1):
        cnt = tangerine.index(temp[i+1])
        tp.append(cnt - num)
        num = cnt
    tp.append((len(tangerine)) - tangerine.index(temp[len(temp)-1]))
    tp.sort(reverse=True)
    for i in tp:
        if i < k :
            k -= i
            answer += 1
        else:
            answer += 1
            break

    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k,tangerine))
