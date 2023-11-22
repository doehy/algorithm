import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
result = 0
data.sort()
for i in range(n):
    left, right = 0, n-1
    while left < right:
        if data[left] + data[right] == data[i]:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                result += 1
                break
        elif data[left] + data[right] > data[i]:
            right -= 1
        else:
            left += 1
print(result)

# 생각을 해보다가 아무리 해도 시간초과아니면 메모리 초과가 발생할 때 입증하기 어려워도 될 것 같으면 한 번 시도해보자
# 그리고 똑같은 숫자 입력이 주어질 수도 있으니 이 점을 주의하자