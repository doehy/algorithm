from collections import deque

n,k = map(int,input().split())

queue = deque()

for i in range(1,n+1):
    queue.append(i)

num = len(queue)
while num > 0:
    if n == 1:
        print("<"+str(queue[0])+">")
        break
    
    if num == n:
        print("<",end='')
        queue.rotate(-(k-1))
        print(str(queue[0])+",",end=' ')
        queue.remove(queue[0])
        num -= 1
    elif num == 1:
        print(str(queue[0])+'>')
        num -= 1
    else:
        queue.rotate(-(k-1))
        print(str(queue[0])+",",end=' ')
        queue.remove(queue[0])
        num -= 1


