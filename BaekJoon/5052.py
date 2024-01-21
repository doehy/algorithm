import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    flag = 0
    n = int(input())
    numberSet = set()
    data = []
    for _ in range(n):
        data.append(input().rstrip())
    data = sorted(data, key = lambda x : len(x))
    for num in data:
        temp = ''
        for i in range(len(num)):
            if temp+num[i] not in numberSet:
                temp += num[i]
            else:
                flag = 1
                break
        if flag == 1:
            break
        else:
            numberSet.add(temp)
    if flag == 1:
        print("NO")
    else:
        print("YES")
# 일단 길이 순서대로 정렬한다. 그래서 집합에다가 넣어서 있는지 확인한다. 

