number = int(input())

lst = list(map(int,input().split()))

n = len(lst)

if n == 1:
    print(lst[0]**2)
if n>=2:
    print(max(lst)*min(lst))