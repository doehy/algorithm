n = int(input())
number = list(map(int,input().split()))
sign = list(map(int,input().split()))

max_ans = -1000000000
min_ans = 1000000000

def cal (s): # s는 부호들의 idx의 문자열이다.
    temp = 0
    if s[0] == "0":
        temp = number[0] + number[1]
    elif s[0] == "1":
        temp = number[0] - number[1]
    elif s[0] == "2":
        temp = number[0] * number[1]
    else:
        temp = number[0] // number[1]
    for i in range(1,n-1):
        if s[i] == "0":
            temp += number[i+1]
        elif s[i] == "1":
            temp -= number[i+1]
        elif s[i] == "2":
            temp *= number[i+1]
        else:
            if temp < 0:
                temp = -1 * (-1 * temp // number[i+1])
            else:
                temp //= number[i+1]
    return temp # 계산이 완료된 수

def solve(s,sign): # 남은 갯수가 0보다 크거나 아니면 
    global max_ans, min_ans
    if len(s) == n-1:
        temp = cal(s) # s는 부호의 수열이다.
        max_ans = max(max_ans,temp)
        min_ans = min(min_ans,temp)
        return
    for i in range(4): # 부호는총 4개있으니까
        if sign[i]: # 남은 갯수가 있다면
            sign[i] -= 1
            solve(s+str(i),sign)
            sign[i] += 1
            

s = ""
solve(s,sign)
print(max_ans)
print(min_ans)