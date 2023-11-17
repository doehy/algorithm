import sys
input = sys.stdin.readline


n = int(input())
data = [[] for i in range(n+1)]
text_idx = [0] * n
sum = 0
for i in range(n+1):
    text = input().strip('\n')
    t_word = ''
    for j in text:
        if j != ' ':
            t_word = t_word + j
        else:
            sum += 1
            data[i].append(t_word)
            t_word = ''
    sum += 1
    data[i].append(t_word)
word = ""
flag = 0
def check(word):
    global flag
    for i in range(n):
        if text_idx[i] < len(data[i]):
            if data[i][text_idx[i]] == word:
                text_idx[i] += 1
                flag = 0
                return flag
            else:
                flag = 1
    return flag


for word in data[len(data)-1]:
    check(word)
    if flag == 1:
        print("Impossible")
        break

sum -= len(data[len(data)-1])
if flag != 1:
    if len(data[len(data)-1]) < sum:
        print("Impossible")
    elif len(data[len(data)-1]) > sum:
        print("Impossible")
    else:
        print("Possible")



