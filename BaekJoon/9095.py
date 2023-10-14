n = int(input())

def check(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return check(n-1) + check(n-2) + check(n-3)


for i in range(n):
    num = int(input())
    print(check(num))