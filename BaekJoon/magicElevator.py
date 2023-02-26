def solution(storey):
    answer = 0
    bf = 0
    strstor = str(storey)
    for i in range(len(strstor)-1,-1,-1):
        af = 0
        if i >=  1:
            af = int(strstor[i-1])
        if bf == 1:
            temp = int(strstor[i]) + 1
            bf = 0
        else:
            temp = int(strstor[i])
        if temp <= 5:
            if temp == 5 and af >= 5:
                bf = 1
            answer += temp
        else:
            answer += 10 - temp
            bf = 1
    if bf == 1:
        answer += 1
    return answer
#원래는 5이하이면 내리고 초과면 올라갈려했지만 내 앞에 것이 6이상이라면 5까지는 올라가는게 맞다.
print(solution(54))
