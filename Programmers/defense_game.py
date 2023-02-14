result = 0
n = 6
k = 0
enemy = [1, 1, 1, 1, 1, 1, 1]

def check(idx,numk,defense):
    print(idx,numk,defense)
    global result
    result = max(result,idx)
    if idx == len(enemy):
        return
    if defense < enemy[idx]:
        return
    if numk < k:
        check(idx+1,numk+1,defense)
    check(idx+1,numk,defense-enemy[idx])

def solution(n, k, enemy):
    answer = 0
    if k >= len(enemy) or n >= sum(enemy):
        answer = len(enemy)
    else:
        check(0,0,n)
    return answer

solution(n,k,enemy)
print(result)