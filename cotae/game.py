N,M = map(int,input().split())

A,B,direction = map(int,input().split())

d = [[0]*M for _ in range(N)]
d[A][B] = 1

array = []

for i in range(N):
    array.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
number = 0

while True:
    if number == 4:
        number = 0
        for i in range(2):
            turn_left()
        A = A + dx[direction]
        B = B + dy[direction]
        if array[A][B] == 1:
            break
        else:
            for i in range(2):
                turn_left()

    turn_left()
    number += 1
    if array[A+dx[direction]][B+dy[direction]] == 1:
       continue
    else:
        if d[A+dx[direction]][B+dy[direction]] == 0:
            count += 1
            A = A + dx[direction]
            B = B + dy[direction]
            d[A][B] = 1
            number = 0
        else: #육지이나 가봤던 경험이 있는 경우
            continue

    

print(count)

        