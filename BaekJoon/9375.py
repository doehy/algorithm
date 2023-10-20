t = int(input())

for i in range(t):
    answer = dict()
    n = int(input())
    for i in range(n):
        name,c_type = input().split()
        if c_type not in answer:
            answer[c_type] = 1
        else:
            answer[c_type] += 1
    result = 1
    for i in answer:
        result *= (answer[i] + 1)
    result -= 1
    print(result)            