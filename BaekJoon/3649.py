import sys
input = sys.stdin.readline
while True:
    try:
        holl = int(input()) * (10 ** 7)
        n = int(input())
        robot = list()
        for _ in range(n):
            robot.append(int(input()))
        ans = 0
        if len(robot) < 2:
            print("danger")
            continue
        robot.sort()
        left, right = 0, n-1
        flag = 0
        while left < right:
            if robot[left] + robot[right] == holl:
                print("yes", robot[left], robot[right])
                flag = 1
                break
            elif robot[left] + robot[right] > holl:
                right -= 1
            else:
                left += 1
        if not flag:
            print("danger")
    except:
        break