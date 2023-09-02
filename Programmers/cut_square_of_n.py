def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        if b > a: a,b = b,a
        answer.append(a+1)
    return answer

# n의 크기가 시간 상 말이 안 됐다. 차선책 1차원으로 풀어보려고도 했는데 이것도 시간 상 말이 안 됐다. 
# 차선책을 생각했을 때도 시간 상 말이 안 될 때 한번 규칙을 찾아보자