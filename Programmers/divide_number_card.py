# 숫자 카드 나누기 한 번 최대 공약수 문제를 풀어보자 이거 문제에서 정렬 돼있따고 나와있지도 않은데 사람들이 정렬돼있다는 기준으로 푼 것 같다.
from math import gcd
def get_gcd(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g

def solution(arrayA, arrayB):
    answer = 0
    a,b = get_gcd(arrayA), get_gcd(arrayB)

    if a != 0:
        flag = 0
        for num in arrayB:
            if num % a == 0:
                flag = 1
                break
        if flag == 0:
            answer = max(answer, a)
    if b != 0: 
        flag = 0
        for num in arrayA:
            if num % b == 0:
                flag = 1
                continue
        if flag == 0:
            answer = max(answer, b)
        return answer


arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
print(solution(arrayA, arrayB))