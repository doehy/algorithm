import sys
input = sys.stdin.readline

N = int(input())

people = []
for i in range(N):
    people.append(input().rstrip())
finish = []
for i in range(N-1):
    finish.append(input().rstrip())

people.sort()
finish.sort()

flag = 0
for i in range(N-1):
    if people[i] != finish[i]:
        print(people[i])
        flag = 1
        break

if flag == 0:
    print(people[-1])