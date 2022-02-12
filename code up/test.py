from collections import deque

queue = deque()
lst = list()
N,M = map(int,input().split())


lst.append(input().split())

number = 0 #while문 도는 횟수
l_num = 0 #왼쪽으로 도는 횟수
r_num = 0 #오른쪽으로 도는 횟수
num = 0 #더해지는 숫자
score = 0 #최솟값 개수

while number < M:
    queue.clear()
    for j in range(1,N+1):
        queue.append(j)
    while lst[i] != queue[0]:
        queue.rotate(1)
        r_num += 1
    queue.clear()
    for k in range(1,N+1):
        queue.append(k)
    while lst[i] != queue[0]:
        queue.rotate(-1)
        l_num += 1
    num = r_num if r_num > l_num else l_num
    score += num
    
    

print(score)
