import sys

while True:
    nums = list(map(int, sys.stdin.readline().split())) #일단 입력을 받는다.
    if nums[0] == 0: #0을 입력받았을 시 탈출한다.
        break

    nums.pop(0) #맨 앞에 숫자는 집합의 개수를 나타내는 것이니 pop해서 없애준다.
    V = 6 # V == 6이라는 것은 그냥 집합은 6개까지 골라야하기 때문에 만들어 둔 변수이다.
    stack = [] #스택이라는 리스트를 만들 것이다.


    def dfs():
        if len(stack) == V:
            print(*stack)
            return
        
        if len(stack) == 0:
            for i in nums:
                stack.append(i)
                dfs()
                stack.pop()
            return

        for i in nums:
            if i > stack[len(stack)-1]:
                stack.append(i)
                dfs()
                stack.pop()

    dfs()
    print()