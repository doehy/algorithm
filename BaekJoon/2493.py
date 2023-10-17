import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
stack = [(data[-1],n-1)]
answer = [0] * n
for i in range(n-2,-1,-1): # 끝에서 두번째꺼부터 처음꺼까지만
    while len(stack) > 0 and data[i] > stack[-1][0]: # 스택이 0 이상이고 현재 값이 이미 스택에 있던 값보다 큰 동안
        answer[stack[-1][1]] = i + 1 # answer값 표시하고
        stack.pop() # stack 젤 위 값을 없앤다.
    stack.append((data[i], i))
print(*answer)

# 스택 형식상 점점 작아지는 형태로만 스택에 쌓이게 된다.
        


# 입력의 개수가 최대 오십만 무식하게 반복하면 무조건 시간초과이고
# 정렬하면 안 돼
# 6 9 5 7 4 