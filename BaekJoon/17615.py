import sys
input = sys.stdin.readline
n = int(input())
ball = list(input().rstrip())
ans = float("inf")
def left_move_red(ball):
    global ans
    flag = 0
    cnt = 0
    for i in range(len(ball)):
        if flag == 1:
            if ball[i] == 'R':
                cnt += 1
        else:
            if ball[i] == 'B':
                flag = 1
    ans = min(ans, cnt)

def right_move_red(ball):
    global ans
    flag = 0
    cnt = 0
    for i in range(len(ball)-1, -1, -1):
        if flag == 1:
            if ball[i] == 'R':
                cnt += 1
        else:
            if ball[i] == 'B':
                flag = 1
    ans = min(ans, cnt)
def left_move_blue(ball):
    global ans
    flag = 0
    cnt = 0
    for i in range(len(ball)):
        if flag == 1:
            if ball[i] == 'B':
                cnt += 1
        else:
            if ball[i] == 'R':
                flag = 1
    ans = min(ans, cnt)

def right_move_blue(ball):
    global ans
    flag = 0
    cnt = 0
    for i in range(len(ball)-1, -1, -1):
        if flag == 1:
            if ball[i] == 'B':
                cnt += 1
        else:
            if ball[i] == 'R':
                flag = 1
    ans = min(ans, cnt)

left_move_blue(ball)
left_move_red(ball)
right_move_blue(ball)
right_move_red(ball)
print(ans)

# 아 처음에 했던 생각이 맞았다.
