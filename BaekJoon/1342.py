from itertools import permutations

text = list(input())

def check(num):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return 0
    return 1
data = dict()
for i in text:
    if i not in data:
        data[i] =  1
    else:
        data[i] += 1

count = 0
tp = set()
for num in permutations(text, len(text)):
    count += check(num)

def cal(num):
    if num == 1:
        return 1
    else:
        return num * cal(num - 1)
total = 1
for i in data.keys():
    total *= cal(data[i]) 
count //= total
print(count)
# 무슨 기준은 없을 것 같애
# 모든 경우의 수를 다 들여봐야 될 것 같음
# 문자열 길이도 최대 10 밖에 안 되네

# 위치에 들어가고 안 들어가고라고 생각하는데 다른 방법이 있을 수도
# 어떻게 모든 경우를 다 들어가냐 
