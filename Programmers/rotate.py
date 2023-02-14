from collections import deque
def solution(s):
    answer = 0
    for i in range(len(s)):
        data = deque(s)
        data.rotate(-i)
        temp = []
        flag = 0
        for j in data:
            print(temp)
            if j == '(' or j == '{' or j == '[':
                temp.append(j)
            else:
                if len(temp) == 0:
                    flag = 1
                    break
                if (j == ')' and temp[len(temp)-1] != '(') or (j == '}' and temp[len(temp)-1] != '{') or (j == ']' and temp[len(temp)-1] != '['):
                    flag = 1
                    break
                else:
                    temp.pop()
        if flag == 0 and len(temp) == 0:
            answer += 1 
    return answer

s = "()("
print(solution(s))