n = int(input())
data = list(map(int,input().split()))
data.sort()

left, right = 0, n-1

answer = abs(data[left] + data[right])
final = [data[left], data[right]]

while left < right:
    left_val = data[left]
    right_val = data[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])

# -99, -2, -1, 4, 98
# 부호가 같다면 붙어있어야 가장 작은 값을 내고 부호가 다르면 멀리 떨어져 있어도 된다.