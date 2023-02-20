n,m = map(int,input().split())

data = list(map(int,input().split()))
data.append(0)
data.sort()
zero_idx = data.index(0)

# 왼쪽 *1, 오른쪽 * 1

def left_multione():
    count = 0
    if zero_idx == 0:
        return float("inf")
    i = 0
    flag = 0
    while i < zero_idx:
        if flag == 0:
            count += abs(data[i])
            flag = 1
        else:
            count += abs(data[i]) * 2
        i += m
    i = len(data) - 1
    while i > zero_idx:
        count += abs(data[i]) * 2
        i -= m
    return count
def right_multione():
    count = 0
    if zero_idx == len(data) - 1:
        return float("inf")
    flag = 0
    i = len(data) - 1
    while i > zero_idx:
        if flag == 0:
            count += abs(data[i])
            flag = 1
        else:
            count += abs(data[i]) * 2
        i -= m
    i = 0
    while i < zero_idx:
        count += abs(data[i]) * 2
        i += m
    return count
result = float("inf")
result = min(result,left_multione())
result = min(result,right_multione())
print(result)





