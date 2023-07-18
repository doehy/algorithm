def isPrime(number):
    if number < 2:
        return 0
    for i in range(2,int(number ** 0.5)+1):
        if number % i == 0:
            return 0
    return 1

def check(number):
    if len(number) > 0:
        return isPrime(int(number))
    return 0

def solution(n, k):
    answer = 0
    temp = []
    while n != 0:
        temp.append(str(n%k))
        n //= k
    temp.reverse()
    num = ''.join(temp)
    first_flag = 0
    idx = 0
    number = ''
    while first_flag == 0 and idx < len(num):
        if num[idx] == '0':
            answer += check(number)
            first_flag = 1
            idx += 1
            break
        number += num[idx]
        idx += 1
    if first_flag == 0: # 0인 상태로 나왔다는 것은 주어진 숫자에서 0이 하나도 없었다는 의미이다.
        answer += isPrime(int(number)) # 그러니 바로 리턴
        return answer
    number = ''
    for i in range(idx,len(num)):
        if num[i] == '0':
            answer += check(number)
            number = ''
        number += num[i]
    answer += check(number) #number에 숫자가 남아있을 수도 있으니까
    return answer