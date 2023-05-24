import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
before = []
for i in range(k):
    before.append(chr(65+i))    
after = list(input().rstrip())
data = []
for i in range(n):
    data.append(list(input().rstrip()))

flag = 0
for i in range(len(data)):
    j = 0
    while j < k - 1:
        if data[i][j] == '?':
            flag = 1
            break        
        if data[i][j] == '-':
            before[j], before[j+1] = before[j+1], before[j]
            j += 2
            continue
        j += 1
    if flag == 1:
        break

flag = 0
for i in range(len(data)-1,-1,-1):
    j = 0
    while j < k - 1:
        if data[i][j] == '?':
            flag = 1
            break
        if data[i][j] == '-':
            after[j], after[j+1] = after[j+1], after[j]
            j += 2
            continue
        j += 1
    if flag == 1:
        break

answer = ""
i = 0
while i < k-1: # 문자의 갯수
    if before[i] == after[i]:
        answer += "*"
        i += 1
    elif before[i] == after[i+1]:
        if i != k - 2: # k가 10이라 했을 때 8이 아니라면 즉 8이라는 뜻은 8과 9사이를 본다는 의미니 
            answer += "-*"
        else:
            answer += "-"
        i += 2
    else:
        answer = "x" * (k-1)
        break
print(answer)